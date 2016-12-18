from django import forms

from .models import Partida


class FormularioPartida(forms.ModelForm):

    class Meta:
        # modelo usado para el formulario de Partida en la vista crear_partida
        model = Partida
        # el atributo de Partida que no quiero que aprezca en la view
        exclude = ('jugando','turnos','pieza_en_juego')
        
        fields = '__all__'
        