from django.db import models

# Create your models here.
from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField(
        null=True,
        blank=True,
    )
    codigo = models.CharField(
        max_length=30,
        unique=True,
    )

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
