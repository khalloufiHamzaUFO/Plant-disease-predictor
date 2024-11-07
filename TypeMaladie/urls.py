from django.urls import path
from .views import delete_type_maladie, type_maladie_list, home, create_type_maladie, type_maladie_list_farmer
from .views import TypeMaladieCreateView, TypeMaladieUpdateView, TypeMaladieDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('typemaladiesfarmer/', type_maladie_list_farmer, name='type_maladie_list_farmer'),
    path('typemaladies/', type_maladie_list, name='type_maladie_list'),
    path('typemaladies/create/', create_type_maladie, name='type_maladie-create'),
    path('typemaladies/<int:pk>/update/', TypeMaladieUpdateView.as_view(), name='type_maladie_update'),
    path('typemaladies/<int:pk>/delete/', delete_type_maladie, name='delete_type_maladie'),  # Nom cohérent
]
