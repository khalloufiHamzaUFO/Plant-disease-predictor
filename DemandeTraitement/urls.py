# DemandeTraitement/urls.py
from django.urls import path
from .views import DemandeTraitementCreateView, DemandeTraitementListView, DemandeTraitementUpdateView, DemandeTraitementDeleteView, RendezVousCreateView, create_rendezvous, createDemande

urlpatterns = [
    path('demandes/create/<int:pk>', createDemande, name='demande_create'),  # Vue pour créer une demande
    path('demandes/liste/', DemandeTraitementListView.as_view(), name='demande_list'),  # Vue pour lister les demandes
    path('update/<int:pk>/', DemandeTraitementUpdateView, name='demande_update'),  # Route pour la mise à jour
    path('delete/<int:pk>/', DemandeTraitementDeleteView, name='demande_delete'),
    path('rendezvous/create/',create_rendezvous, name='rendezvous_create'),
    path('rendezvous/create/<int:demande_id>/', create_rendezvous, name='rendezvous_create'),
  
]
