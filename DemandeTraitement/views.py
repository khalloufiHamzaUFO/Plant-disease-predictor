# DemandeTraitement/views.py
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from PlantApp.models import DiseaseDetection
from .models import DemandeTraitement, RendezVous
from .forms import DemandeTraitementForm, RendezVousForm

from django.urls import reverse_lazy



def createDemande(request, pk):
    disease = get_object_or_404(DiseaseDetection, id=pk)
    if request.method == 'POST':
        form = DemandeTraitementForm(request.POST)
        if form.is_valid():
            demande = form.save(commit=False)
            demande.status = "en_attente"
            demande.title_desease = disease.plant.name  +" is problem in "+ disease.detected_disease
            demande.save()
            disease.demande = demande 
            disease.save()
            return redirect('PlantApp:details_plant', pk=disease.plant.id)
    else:
        form = DemandeTraitementForm()
    return render(request, 'demande_traitement/create.html', {'form': form, 'disease': disease})

class DemandeTraitementCreateView(CreateView):
    model = DemandeTraitement
    form_class = DemandeTraitementForm
    template_name = 'demande_traitement/create.html'  # Vérifie que le chemin est correct
    success_url = reverse_lazy('demande_list')  # Assure-toi que cette URL est bien définie

class DemandeTraitementListView(ListView):
    model = DemandeTraitement
    template_name = 'demande_traitement/list.html' 
    context_object_name = 'demandes' 
def DemandeTraitementUpdateView(request, pk):
    demande = get_object_or_404(DemandeTraitement, pk=pk)
    if request.method == 'POST':
        form = DemandeTraitementForm(request.POST, instance=demande)
        if form.is_valid():
            form.save()
            return redirect('demande_list')  # Rediriger vers la liste après mise à jour
    else:
        form = DemandeTraitementForm(instance=demande)
    return render(request, 'demande_traitement/create.html', {'form': form})

# Vue pour supprimer une demande de traitement
def DemandeTraitementDeleteView(request, pk):
    demande = get_object_or_404(DemandeTraitement, pk=pk)
    if request.method == 'POST':
        demande.delete()
        return redirect('demande_list')  # Rediriger vers la liste après suppression
    return render(request, 'demande_traitement/confirm_delete.html', {'demande': demande})


def create_rendezvous(request, demande_id):
    # Get the DemandeTraitement instance or simulate details if needed
    demande = get_object_or_404(DemandeTraitement, pk=demande_id)
    
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            rendezvous = form.save(commit=False)
            rendezvous.demande = demande  # Associate the rendezvous with the demande
            demande.status = "approuve"
            demande.save()
            rendezvous.save()
            return redirect('demande_list')  # Redirect after successful creation
    else:
        form = RendezVousForm()

    # Pass demande details to the context
    context = {
        'form': form,
        'demande': {
            'id': demande.id,
            'objet': "Objet fictif de la demande"  # Replace with actual details if available
        }
    }

    return render(request, 'demande_traitement/create_rendezvous.html', context)
class RendezVousCreateView(CreateView):
    model = RendezVous
    form_class = RendezVousForm
    template_name = 'demande_traitement/create_rendezvous.html'
    success_url = reverse_lazy('demande_list')  # Redirige après succès

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupérer l'ID de la demande à partir de l'URL
        demande_id = self.kwargs.get('demande_id')
        # Simuler des détails de la demande sans utiliser un modèle
        context['demande'] = {
            'id': demande_id,
            'objet': "Objet fictif de la demande"  # Remplacez par les détails réels si disponibles
        }
        return context

    def form_valid(self, form):
        demande_id = self.kwargs.get('demande_id')
        if demande_id:
            form.instance.demande_id = demande_id  # Associer l'ID à votre instance de rendez-vous
            return super().form_valid(form)
        else:
            return redirect(self.success_url)
            
class DemandeTraitementDetailView(DetailView):
    model = DemandeTraitement
    template_name = 'demande_detail.html'  # Remplacez par votre modèle de template
    context_object_name = 'demande'
