from django.db import models

# Modelo para las tecnologías
class Tecnologias(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='tecnologias')

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'
        
    def __str__(self) -> str:
        return self.nombre

# Modelo para los proyectos
class Proyectos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos')
    tecnologias = models.ManyToManyField(Tecnologias, related_name='proyectos')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.nombre
    
    def tecnologias_list(self):
        return ", ".join([tecnologia.nombre for tecnologia in self.tecnologias.all()])

    tecnologias_list.short_description = 'Tecnologías'
    

# Guardar las imágenes en una carpeta específica dentro de 'galeria_proyectos'
# y agregar un campo para texto alternativo
class ImagenProyecto(models.Model):
    proyecto = models.ForeignKey(Proyectos, related_name='imagenes_proyecto', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='galeria_proyectos')
    alt_text = models.CharField(max_length=255, blank=True, null=True, verbose_name='Texto Alternativo')

    class Meta:
        verbose_name = 'Imagen del Proyecto'
        verbose_name_plural = 'Imágenes del Proyecto'

    def __str__(self):
        return f"Imagen de {self.proyecto.nombre}"
    
# Modelo para las redes sociales
class Redes(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.URLField()
    icono = models.ImageField(upload_to='redes')

    class Meta:
        verbose_name = 'Red'
        verbose_name_plural = 'Redes'

    def __str__(self) -> str:
        return self.nombre

# Mi información personal
class SobreMi(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='sobre_mi')
    redes = models.ManyToManyField(Redes, related_name='redes', blank=True)

    class Meta:
        verbose_name = 'Sobre_mi'
        verbose_name_plural = 'Sobre_mi'

    def __str__(self) -> str:
        return self.nombre


