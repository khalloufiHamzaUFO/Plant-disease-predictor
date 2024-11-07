# methodeTraitementApp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import MethodeTraitement
from .forms import MethodeTraitementForm  # Assurez-vous d’avoir ce formulaire
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def methode_traitement_list(request):
    methodes = MethodeTraitement.objects.all()
    return render(request, 'methode_traitement_list.html', {'methodes': methodes})

def create_methode_traitement(request):
    if request.method == 'POST':
        form = MethodeTraitementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('methode_traitement_list')
    else:
        form = MethodeTraitementForm()
    
    return render(request, 'methode_traitement_form.html', {'form': form})

class MethodeTraitementCreateView(CreateView):
    model = MethodeTraitement
    form_class = MethodeTraitementForm
    template_name = 'methode_traitement_form.html'
    success_url = reverse_lazy('methode_traitement_list')

class MethodeTraitementUpdateView(UpdateView):
    model = MethodeTraitement
    form_class = MethodeTraitementForm
    template_name = 'methode_traitement_update_form.html'
    success_url = reverse_lazy('methode_traitement_list')

class MethodeTraitementDeleteView(DeleteView):
    model = MethodeTraitement
    template_name = 'methode_traitement_confirm_delete.html'
    success_url = reverse_lazy('methode_traitement_list')

def methode_traitement_detail(request, pk):
    methode = get_object_or_404(MethodeTraitement, pk=pk)
    return render(request, 'methode_traitement_detail.html', {'methode': methode})
