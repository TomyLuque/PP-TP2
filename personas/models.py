from django.db import models
from oficinas.models import Oficina

class Persona(models.Model):
    # Persona tranqui: lo mínimo para el práctico.
    apellido = models.CharField(max_length=120)
    nombre = models.CharField(max_length=120)
    edad = models.PositiveIntegerField()
    oficina = models.ForeignKey(Oficina, on_delete=models.PROTECT, related_name='personas')

    class Meta:
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
