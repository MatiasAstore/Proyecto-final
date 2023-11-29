from django.contrib import admin
from .models import Educacion, Proyectos, Persona, EducacionComplementaria, Experiencia, MensajeContacto

# Register your models here.

admin.site.register(Educacion)
admin.site.register(Proyectos)
admin.site.register(EducacionComplementaria)
admin.site.register(Experiencia)
admin.site.register(Persona)
admin.site.register(MensajeContacto)

