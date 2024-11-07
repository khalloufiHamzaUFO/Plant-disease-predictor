# forms.py
from django import forms
from .models import Maladie
from TraitementApp.models import Treatment  # Import Treatment model

class MaladieForm(forms.ModelForm):
    # Add traitements field to select multiple treatments
    traitements = forms.ModelMultipleChoiceField(
        queryset=Treatment.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Maladie
        fields = ['nom', 'description', 'image', 'causes', 'symptomes', 'types', 'traitements']  # Add 'traitements' here
        
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la maladie'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description de la maladie'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'causes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Causes de la maladie'}),
            'symptomes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Symptômes observables'}),
            'types': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'traitements': forms.SelectMultiple(attrs={'class': 'form-control'}),  # Widget for traitements
        }
