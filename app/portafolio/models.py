from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete,post_migrate
from django.dispatch import receiver

class Usuario(AbstractUser):
    imagen = models.ImageField(upload_to='perfil/', null=True )

class IconoSVG(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.TextField()  # SVG como texto

    def __str__(self):
        return self.nombre


class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50)
    icono_svg = models.ForeignKey(IconoSVG, on_delete=models.SET_NULL, blank=True, null=True)
    icono_imagen = models.ImageField(upload_to='tecnologias/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    enlace = models.URLField(blank=True, null=True)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo

# Define la función para crear el usuario admin
def crear_usuario_admin(**kwargs):
    if not Usuario.objects.filter(username='gladoncio').exists():
        Usuario.objects.create_superuser(username='gladoncio', password='123')
        print("Usuario administrador creado exitosamente.")

@receiver(post_migrate)
def post_migrate_callback(sender, **kwargs):
    crear_usuario_admin(**kwargs)


