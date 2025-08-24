from django.contrib import admin
from .models import Oficina
@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nombre_corto')
    search_fields = ('nombre', 'nombre_corto')
