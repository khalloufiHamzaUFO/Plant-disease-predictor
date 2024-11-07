# feedback/forms.py
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['prevention', 'content', 'rating', 'date_created']

        widgets = {
            'prevention': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your feedback...'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5, 'placeholder': 'Rate out of 5'}),
            'date_created': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
