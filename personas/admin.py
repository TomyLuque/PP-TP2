from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'apellido', 'nombre', 'edad', 'oficina')
    list_filter = ('oficina',)
    search_fields = ('apellido','nombre')
