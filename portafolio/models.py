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
    





