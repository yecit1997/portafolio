from django.shortcuts import render, get_object_or_404
# from django.contrib import messages
from .models import Proyectos, Tecnologias


def sobre_mi(request):
    return render(request, 'portafolio/sobremi.html')

def home(request):
    proyectos = Proyectos.objects.all()
    tecnologias = Tecnologias.objects.all()
    
    context = {
        'proyectos': proyectos,
        'tecnologias': tecnologias,
    }
    return render(request, 'portafolio/index.html',context=context)


def proyectos(request):
    return render(request, 'proyectos/proyectos.html',)


def ver_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyectos, id=proyecto_id)
    tecnologia = Tecnologias.objects.filter(proyectos=proyecto)
    context = {
        'proyecto': proyecto,
        'tecnologia': tecnologia,
    }
    return render(request, 'proyectos/ver_proyecto.html', context=context)



