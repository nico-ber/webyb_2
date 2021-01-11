from django.db import models

# Create your models here.

class servicio(models.Model):
    icono = models.TextField(max_length=20000)
    titulo = models.CharField(max_length=30, help_text="Título")
    descripcion = models.TextField(max_length=200, help_text="Descripción")
    descripcion2 = models.TextField(max_length=400, help_text="Descripción2", blank=True)
    listado = models.TextField(max_length=1000, help_text="Listado", blank=True)

    def __str__(self):
        return self.titulo
