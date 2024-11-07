from django.urls import path
from .views import treatment_list, create_treatment,    treatment_detail, TreatmentCreateView, TreatmentUpdateView, TreatmentDeleteView

urlpatterns = [
    path('treatments/', treatment_list, name='treatment_list'),
    path('treatments/create/<int:pk>/', create_treatment, name='treatment-create'),
    path('treatments/<int:pk>/update/', TreatmentUpdateView.as_view(), name='treatment-update'),
    path('treatments/<int:pk>/delete/', TreatmentDeleteView.as_view(), name='treatment-delete'),
    path('treatments/<int:pk>/', treatment_detail, name='treatment-detail'),  
    path('treatments/<int:pk>/update/', TreatmentUpdateView.as_view(), name='treatment-update'),

]
