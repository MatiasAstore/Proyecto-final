from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return (
            f"{self.nombre} {self.apellido}"
            if self.nombre and self.apellido
            else "Persona sin nombre"
        )


class Educacion(models.Model):
    establecimiento = models.CharField(max_length=40)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.establecimiento}"


class EducacionComplementaria(models.Model):
    establecimiento = models.CharField(max_length=40)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.establecimiento}"


class Experiencia(models.Model):
    empresa = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.empresa}"


class Proyectos(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to= "projectos", null = True)

    def __str__(self):
        return f"{self.nombre}"


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre


