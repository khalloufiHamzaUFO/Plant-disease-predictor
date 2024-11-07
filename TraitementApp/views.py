from django.shortcuts import render, redirect, get_object_or_404

from Maladie.models import Maladie
from .models import Treatment
from .forms import TreatmentForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from UserApp.decorators import role_required
@login_required 
@role_required("DOCTOR")
def treatment_list(request):
    treatments = Treatment.objects.all()  
    return render(request, 'treatment_list.html', {'treatments': treatments})
@login_required 
@role_required("DOCTOR")
def create_treatment(request, pk):
    if request.method == 'POST':
        maladie = get_object_or_404(Maladie, id=pk)
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            treatment = form.save()
            maladie.traitements.add(treatment)
            return redirect('treatment_list') 
    else:
        form = TreatmentForm()
    return render(request, 'treatment_form.html', {'form': form})

class TreatmentCreateView(CreateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = 'treatment_form.html'
    success_url = reverse_lazy('treatment_list')

class TreatmentUpdateView(UpdateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = 'treatment_update_form.html'  # This will be a separate page for updating
    success_url = reverse_lazy('treatment_list')

class TreatmentDeleteView(DeleteView):
    model = Treatment
    template_name = 'treatment_confirm_delete.html'
    success_url = reverse_lazy('treatment_list')
@login_required 
@role_required("DOCTOR")
def treatment_detail(request, pk):
    treatment = get_object_or_404(Treatment, pk=pk)
    return render(request, 'treatment_detail.html', {'treatment': treatment})
