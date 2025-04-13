from django.shortcuts import render, get_object_or_404
# from django.contrib import messages
from .models import Proyectos, Tecnologias



def home(request):
    return render(request, 'portafolio/index.html')


def sobre_mi(request):
    return render(request, 'portafolio/sobremi.html')

def ver_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyectos, id=proyecto_id)
    tecnologia = Tecnologias.objects.filter(proyectos=proyecto)
    context = {
        'proyecto': proyecto,
        'tecnologia': tecnologia,
    }
    return render(request, 'proyectos/ver_proyecto.html', context=context)