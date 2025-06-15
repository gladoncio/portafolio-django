from .models import IconoSVG

def iconos_globales(request):
    iconos = IconoSVG.objects.all()
    return {icono.nombre: icono for icono in iconos}
