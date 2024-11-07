from django.db import models
from django.conf import settings
from TypeMaladie.models import TypeMaladie  
from TraitementApp.models import Treatment  

class Maladie(models.Model):
    nom = models.CharField(max_length=200, unique=True, verbose_name="Nom de la maladie")
    description = models.TextField(verbose_name="Description de la maladie")
    image = models.ImageField(upload_to='maladies/', verbose_name="Image de la maladie", null=True, blank=True)
    causes = models.TextField(verbose_name="Causes de la maladie", blank=True)
    symptomes = models.TextField(verbose_name="Symptomes observables", blank=True)
    date_publication = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='maladies', null=True)
    types = models.ManyToManyField(TypeMaladie, related_name='maladies', verbose_name="Types de maladies")

    traitements = models.ManyToManyField(Treatment, related_name="maladies", verbose_name="Traitements")

    class Meta:
        verbose_name = "Maladie"
        verbose_name_plural = "Maladies"
        ordering = ['-date_publication']

    def __str__(self):
        return self.nom
