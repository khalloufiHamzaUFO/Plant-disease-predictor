from django.db import models
from django.conf import settings

class TypeMaladie(models.Model):
    nom = models.CharField(max_length=200, unique=True, verbose_name="Nom de la type de maladie")
    description = models.TextField(verbose_name="Description de la type de maladie")
    image = models.ImageField(upload_to='typemaladies/', verbose_name="Image de la type de maladie", null=True, blank=True)
    is_contagious = models.BooleanField(default=True) 
    date_publication = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='typemaladies', null=True)

    class Meta:
        verbose_name = "TypeMaladie"
        verbose_name_plural = "TypeMaladie"
        ordering = ['-date_publication']

    def __str__(self):
        return self.nom
