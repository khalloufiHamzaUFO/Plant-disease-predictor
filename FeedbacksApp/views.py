from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from PreventionApp.models import Prevention  # Updated import
from .forms import FeedbackForm
from django.urls import reverse_lazy
from django.views.generic.edit import  UpdateView, DeleteView
from django.views import View


def feedback_list(request, prevention_id):
    prevention = get_object_or_404(Prevention, pk=prevention_id)
    feedbacks = Feedback.objects.filter(prevention=prevention)  
    
    return render(request, 'feedback_list.html', {
        'prevention': prevention,
        'feedbacks': feedbacks,
    })

def feedback_all(request):
    feedbacks = Feedback.objects.all()  # Retrieve all feedbacks
    return render(request, 'myfeedback.html', {
        'feedbacks': feedbacks,
    })

class FeedbackUpdateView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback_update_form.html'  # Ensure this file exists
    context_object_name = 'feedback'

    def get_success_url(self):
        return reverse_lazy('feedback_all')  # Redirect after update


class FeedbackDeleteView(View):
    def post(self, request, pk):
        feedback = get_object_or_404(Feedback, pk=pk)
        feedback.delete()
        return redirect('feedback_all')  # Redirect to the feedback overview page