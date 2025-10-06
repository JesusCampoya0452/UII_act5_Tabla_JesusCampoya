from django.db import models

class producto(models.Model): # Por convención, los nombres de clases en Python son en PascalCase (Producto en lugar de producto)
    nombre = models.CharField(max_length=100)
    fecha_v = models.DateField()
    unidad_med = models.CharField(max_length=3)

    def __str__(self): # Corregido: '__str__' en lugar de '_str_'
        return f"{self.nombre} ({self.fecha_v})" # Un formato más descriptivo
# Create your models here.
