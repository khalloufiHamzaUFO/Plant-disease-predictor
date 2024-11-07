from django import forms
from .models import Treatment, MethodeTraitement

class TreatmentForm(forms.ModelForm):
    methodes_traitement = forms.ModelMultipleChoiceField(
        queryset=MethodeTraitement.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Treatment
        fields = ['name', 'description', 'date_applied', 'success_rate', 'notes', 'methodes_traitement']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Treatment Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Treatment Description'}),
            'date_applied': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'success_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Success Rate', 'step': '0.01'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Notes'}),
            'methodes_traitement': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})  

        }
