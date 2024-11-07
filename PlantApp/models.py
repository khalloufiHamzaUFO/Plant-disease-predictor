from django.db import models
from django.conf import settings

from DemandeTraitement.models import DemandeTraitement

class Plant(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='plants/', blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='plants' , null = True)

    def __str__(self):
        return self.name
    
class DiseaseDetection(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='detections')
    date_detected = models.DateTimeField(auto_now_add=True)
    detected_disease = models.CharField(max_length=255)
    confidence_score = models.FloatField(null = True)
    image = models.ImageField(upload_to='detections/', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    demande = models.ForeignKey(DemandeTraitement , null = True , on_delete= models.CASCADE)
    def __str__(self):
        return f'{self.detected_disease} on {self.plant.name}'

