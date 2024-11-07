# methodeTraitementApp/forms.py

from django import forms
from .models import MethodeTraitement

class MethodeTraitementForm(forms.ModelForm):

    class Meta:
        model = MethodeTraitement
        fields = ['nom', 'description']
        
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Methode Treatment Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Methode Treatment Description'}),
            
        }
