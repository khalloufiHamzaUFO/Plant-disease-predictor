# DemandeTraitement/models.py
from django.db import models
from django.utils import timezone
from UserApp.models import RUser



class DemandeTraitement(models.Model):
    # Disease  = models.ForeignKey(DiseaseDetection, on_delete=models.CASCADE, related_name='demandes' , null = True)
    title_desease = models.CharField(max_length=150 , null = True)
    from_farmer = models.ForeignKey(RUser, on_delete=models.CASCADE, related_name='sent_demandes' , null=True)
    to_doc = models.ForeignKey(RUser, on_delete=models.CASCADE, related_name='received_demandes' , null=True)
    description = models.TextField()
    date_demande = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=[
            ('en_attente', 'En attente'),
            ('approuve', 'Approuvé'),
            ('rejeté', 'Rejeté')
        ],
        default='en_attente'
    )

    def __str__(self):
        return f"Demande de traitement pour  "
class RendezVous(models.Model):
    demande = models.ForeignKey(DemandeTraitement, on_delete=models.CASCADE)  # Lien vers la demande
    date = models.DateTimeField()  # Date et heure du rendez-vous
    commentaire = models.TextField(blank=True, null=True)  # Commentaire facultatif

    def __str__(self):
        return f'Rendez-vous pour {self.demande} le {self.date}'