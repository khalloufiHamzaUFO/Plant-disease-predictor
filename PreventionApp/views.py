from django.shortcuts import render, redirect, get_object_or_404
from .models import Prevention
from .forms import PreventionForm
from FeedbacksApp.forms import FeedbackForm  # Adjusted import for FeedbackForm
from FeedbacksApp.models import Feedback  # Adjusted import for FeedbackForm

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from UserApp.decorators import role_required
@login_required 
@role_required("DOCTOR")
def prevention_list(request):
    preventions = Prevention.objects.all()  
    return render(request, 'prevention_list.html', {'preventions': preventions})
@login_required 
@role_required("DOCTOR")
def create_prevention(request):
    if request.method == 'POST':
        form = PreventionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prevention_list') 
    else:
        form = PreventionForm()
    
    return render(request, 'prevention_form.html', {'form': form})

# Class-based view for creating a new Prevention record
class PreventionCreateView(CreateView):
    model = Prevention
    form_class = PreventionForm
    template_name = 'prevention_form.html'
    success_url = reverse_lazy('prevention_list')  # Redirect to the prevention list after saving

# Class-based view for updating a Prevention record
class PreventionUpdateView(UpdateView):
    model = Prevention
    form_class = PreventionForm
    template_name = 'prevention_update_form.html'  # Separate template for updating Prevention
    success_url = reverse_lazy('prevention_list')

# Class-based view for deleting a Prevention record
class PreventionDeleteView(DeleteView):
    model = Prevention
    template_name = 'prevention_confirm_delete.html'
    success_url = reverse_lazy('prevention_list')

# Function-based view for showing the details of a Prevention record
@login_required 
@role_required("DOCTOR")
def prevention_detail(request, pk):
    prevention = get_object_or_404(Prevention, pk=pk)
    feedbacks = Feedback.objects.filter(prevention=prevention)  
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.prevention = prevention 
            feedback.save()
            return redirect('prevention_detail', pk=prevention.pk)  
    else:
        form = FeedbackForm() 

    return render(request, 'prevention_detail.html', {
        'prevention': prevention,
        'feedbacks': feedbacks,
        'form': form,  
    })
