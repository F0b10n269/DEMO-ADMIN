from django.contrib import admin
from .models import Producto

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "codigo",
        "precio",
        "stock",
        "disponible",
        "fecha_creacion",
    )

    list_filter = (
        "disponible",
        "fecha_creacion",
        "fecha_vencimiento",
    )

    search_fields = (
        "nombre",
        "codigo",
        "descripcion",
    )

    ordering = (
        "nombre",
    )

    readonly_fields = (
        "fecha_creacion",
    )

    list_editable = (
        "precio",
        "stock",
        "disponible",
    )