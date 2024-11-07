from django import forms
from .models import Prevention

class PreventionForm(forms.ModelForm):
    class Meta:
        model = Prevention
        fields = ['title', 'description', 'date_created']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prevention Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Prevention Description'}),
            'date_created': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
