from django.urls import path
from .views import (
    methode_traitement_list,
    create_methode_traitement,
    methode_traitement_detail,
    MethodeTraitementCreateView,
    MethodeTraitementUpdateView,
    MethodeTraitementDeleteView,
)

urlpatterns = [
    path('methodes_traitement/', methode_traitement_list, name='methode_traitement_list'),
    path('methodes_traitement/create/', create_methode_traitement, name='methode_traitement_create'),
    path('methodes_traitement/<int:pk>/', methode_traitement_detail, name='methode_traitement_detail'),
    path('methodes_traitement/<int:pk>/update/', MethodeTraitementUpdateView.as_view(), name='methode_traitement_update'),
    path('methodes_traitement/<int:pk>/delete/', MethodeTraitementDeleteView.as_view(), name='methode_traitement_delete'),
]
