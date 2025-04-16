from django.db import models

class Tecnologias(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='tecnologias')

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'
        
    def __str__(self) -> str:
        return self.nombre

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
    

class Redes(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.URLField()
    icono = models.ImageField(upload_to='redes')

    class Meta:
        verbose_name = 'Red'
        verbose_name_plural = 'Redes'

    def __str__(self) -> str:
        return self.nombre


class SobreMi(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='sobre_mi')
    redes = models.ManyToManyField(Redes, related_name='redes', blank=True)

    class Meta:
        verbose_name = 'Sobre mi'
        verbose_name_plural = 'Sobre mi'

    def __str__(self) -> str:
        return self.nombre


