from django.shortcuts import render, redirect
from .models import Educacion, Proyectos, Persona, EducacionComplementaria, Experiencia
from .forms import ContactoForm


def index(request):
    personas = Persona.objects.all()
    educacion = Educacion.objects.all()
    educacioncomplementaria = EducacionComplementaria.objects.all()
    experiencia = Experiencia.objects.all()
    proyectos = Proyectos.objects.all()

    context = {
        "personas": personas,
        "educacion": educacion,
        "experiencia": experiencia,
        "proyectos": proyectos,
        "educacioncomplementaria": educacioncomplementaria,
    }
    return render(request, "index.html", context)

def contactame(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "index"
            ) 
    else:
        form = ContactoForm()

    return render(request, "contactame.html", {"form": form})
