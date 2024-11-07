from django.shortcuts import render, redirect
import requests
from .models import DiseaseDetection, Plant
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import ImageUploadForm, PlantForm
from django.contrib.auth.decorators import login_required
from UserApp.decorators import role_required
def home(request):
    return render(request, 'home.html')

@login_required 
@role_required("FARMER")
def plant_list(request):
    plants = Plant.objects.all()  
    return render(request, 'plant_list.html', {'plants': plants})
@login_required 
@role_required("FARMER")
def plant_details(request, pk = None):
    plant = Plant.objects.get(id = pk)  
    
    dis = DiseaseDetection.objects.filter(plant = plant).order_by('-date_detected')
    return render(request, 'plant_details.html', {'plant': plant ,'dis' : dis})

@login_required 
@role_required("FARMER")
def create_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plant_list') 
    else:
        form = PlantForm()
    
    return render(request, 'create_plant.html', {'form': form})


@login_required 
@role_required("FARMER")
def predict(request, pk=None):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            
            # Prepare the files to send in the request
            files = {'image': image.file}

            try:
                # Send the image to the external API
                response = requests.post('http://127.0.0.1:5000/submit',
                                          files=files)

                result = None
                if response.status_code == 200:
                    result_data = response.json() 
                    print(result_data)
                    description = result_data.get('desc', 'Unknown')
                    prediction_score = result_data.get('pred' , 'unknown')
                    title = result_data.get('title', 'unknown')
                    prevent = result_data.get('prevent' , 'unknown')
                    plant = Plant.objects.get(id = pk)
                    
                    ds = DiseaseDetection.objects.create(plant = plant , 
                                                        detected_disease=title , 
                                                        image = image,
                                                   
                                                        confidence_score = prediction_score,
                                                        notes =description)
                    ds.save()
                    return render(request, 'predict.html', {'form': form,
                                                             'description': description,
                                                             'title' : title,
                                                                  "prevent" : prevent ,
                                                             'result' : None,
                                                               'success': True})
                else:
                    result = {"error": "Failed to predict. Status code: {}".format(response.status_code)}

            except requests.exceptions.RequestException as e:
                # Handle any request exceptions
                result = {"error": str(e)}

            return render(request, 'predict.html', {'form': form, 'result': result, 'success': True})
    else:
        form = ImageUploadForm()

    return render(request, 'predict.html', {'form': form})

class PlantCreateView(CreateView):
    model = Plant
    fields = ['name', 'scientific_name', 'description', 'image']
    template_name = 'plant_form.html'
    success_url = reverse_lazy('plant_list')    
    def form_valid(self, form):
        form.instance.owner = self.request.user  
        return super().form_valid(form) 


class PlantUpdateView(UpdateView):
    model = Plant
    fields = ['name', 'scientific_name', 'description', 'image']
    template_name = 'plant_form.html'
    success_url = reverse_lazy('plant_list')
    def get_queryset(self):
        return Plant.objects.filter(id=self.kwargs['pk'])



class PlantDeleteView(DeleteView):
    model = Plant
    template_name = 'plant_confirm_delete.html'
    success_url = reverse_lazy('plant_list')

    def get_queryset(self):
        return Plant.objects.filter(owner=self.request.user)