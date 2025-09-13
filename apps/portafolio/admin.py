from django.contrib import admin
from .models import Proyectos, Tecnologias, ImagenProyecto, Redes, SobreMi

class ImagenProyectoInline(admin.TabularInline):  # O usar admin.StackedInline para una presentación diferente
    model = ImagenProyecto
    extra = 1  # Define cuántos formularios vacíos mostrar para agregar imágenes al principio

@admin.register(Proyectos)
class ProyectosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'tecnologias_list')
    search_fields = ('nombre', 'descripcion', 'tecnologias__nombre')
    list_filter = ('tecnologias',)
    ordering = ('nombre',)
    readonly_fields = ('id',)
    inlines = [ImagenProyectoInline]  # Agrega el inline para las imágenes


@admin.register(Tecnologias)
class TecnologiasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    ordering = ('nombre',)


@admin.register(ImagenProyecto)
class ImagenProyectoAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'alt_text', 'imagen')
    list_filter = ('proyecto',)
    search_fields = ('proyecto__nombre', 'alt_text')
    readonly_fields = ('id',)
    

@admin.register(Redes)
class RedesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'url', 'icono_bootstrap')
    search_fields = ('nombre', 'url')
    list_filter = ('nombre',)
    ordering = ('nombre',)
    readonly_fields = ('id',)
    

@admin.register(SobreMi)
class SobreMiAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'imagen')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('nombre',)
    ordering = ('nombre',)
    readonly_fields = ('id',)