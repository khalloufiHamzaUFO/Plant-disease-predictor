from django.urls import path
from .views import plant_list,home ,create_plant , predict,plant_details
from .views import PlantCreateView,PlantUpdateView,PlantDeleteView

app_name = 'PlantApp'

urlpatterns = [
        path('home/', home, name='home'),
        path('plants/', plant_list, name='plant_list'),
        path('plants/create/', create_plant, name='plant-create'),
        path('plants/<int:pk>/', plant_details, name='details_plant'),
        path('plants/<int:pk>/update/', PlantUpdateView.as_view(), name='plant-update'),
        path('plants/<int:pk>/delete/', PlantDeleteView.as_view(), name='plant-delete'),
        path('plants/<int:pk>/predict/', predict, name='predict'),
]
