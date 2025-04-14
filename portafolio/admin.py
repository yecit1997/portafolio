from django.contrib import admin
from .models import Proyectos, Tecnologias

# Register your models here.
@admin.register(Proyectos)
class ProyectosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'tecnologias_list')
    search_fields = ('nombre', 'descripcion', 'tecnologias_list')
    # prepopulated_fields = {'tecnologias_list': ('nombre',)}
    # list_filter = ('tecnologias_list',)
    ordering = ('nombre',)
    readonly_fields = ('id',)
    

@admin.register(Tecnologias)
class TecnologiasAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    # prepopulated_fields = {'tecnologias_list': ('nombre',)}
    # list_filter = ('tecnologias_list',)
    ordering = ('nombre',)
    readonly_fields = ('id',)