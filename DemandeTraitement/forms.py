# DemandeTraitement/forms.py
from django import forms
from .models import DemandeTraitement, RendezVous

class DemandeTraitementForm(forms.ModelForm):
    class Meta:
        model = DemandeTraitement
        fields = [ 'description']
        
    def __init__(self, *args, **kwargs):
        super(DemandeTraitementForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = True  # Rendre le champ description obligatoire
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Décrivez votre demande ici'})  # Ajouter des classes et un placeholder

class RendezVousForm(forms.ModelForm):
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',  # Utilise un type datetime-local pour les navigateurs modernes
            'class': 'datepicker'
        }),
        label="Date et heure"
    )

    class Meta:
        model = RendezVous
        fields = ['date', 'commentaire']