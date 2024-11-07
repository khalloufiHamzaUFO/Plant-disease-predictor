from django.db import models

class MethodeTraitement(models.Model):
    nom = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom
