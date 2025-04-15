from django.db import models

class Desarrollador(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    historia = models.TextField()

    def __str__(self):
        return self.nombre

class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.SET_NULL, null=True)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo