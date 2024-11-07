from django import forms
from .models import TypeMaladie

class TypeMaladieForm(forms.ModelForm):
    class Meta:
        model = TypeMaladie
        fields = ['nom', 'description', 'image', 'is_contagious'] 
         
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la Type Maladie'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description de la Type Maladie'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'is_contagious': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  
        }
