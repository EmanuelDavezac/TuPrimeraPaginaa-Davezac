from django import forms
from .models import Desarrollador, Plataforma, Videojuego

class DesarrolladorForm(forms.ModelForm):
    class Meta:
        model = Desarrollador
        fields = '__all__'

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = '__all__'

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = '__all__'
