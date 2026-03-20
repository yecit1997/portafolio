def redes_context(request):
    from apps.portafolio.models import Redes

    return {"redes": Redes.objects.all()}
