from django.db import models

class Oficina(models.Model):
    # Oficina básica, sin vueltas.
    nombre = models.CharField(max_length=150)
    nombre_corto = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.nombre_corto})"
