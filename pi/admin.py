from django.contrib import admin

# Register your models here.
from .models import PiData, PiConfig

admin.register(PiData, PiConfig)(admin.ModelAdmin)	
