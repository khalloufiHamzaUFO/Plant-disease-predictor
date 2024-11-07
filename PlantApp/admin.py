from django.contrib import admin
from UserApp.models import RUser

from .models import Plant, DiseaseDetection
from DemandeTraitement.models import DemandeTraitement, RendezVous


# Register the CustomUser model using the built-in UserAdmin

# Register the Plant and DiseaseDetection models
admin.site.register(Plant)
admin.site.register(DiseaseDetection)
admin.site.register(DemandeTraitement)
admin.site.register(RendezVous)
