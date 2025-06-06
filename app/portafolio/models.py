from django.db import models

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50)
    icono_svg = models.TextField(blank=True, null=True)  # Puedes almacenar SVG como texto
    icono_imagen = models.ImageField(upload_to='tecnologias/', blank=True, null=True)  # Para archivos

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    enlace = models.URLField(blank=True, null=True)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo