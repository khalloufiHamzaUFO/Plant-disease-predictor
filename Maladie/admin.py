from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from UserApp.models import RUser
from .models import Maladie



admin.site.register(Maladie)
