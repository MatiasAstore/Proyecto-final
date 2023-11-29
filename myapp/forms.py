from django import forms
from .models import MensajeContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ["nombre", "correo", "mensaje"]

    nombre = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    correo = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    mensaje = forms.CharField(
        label="Mensaje", widget=forms.Textarea(attrs={"class": "form-control"})
    )
