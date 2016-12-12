from django import forms

from .models import Partida


class FormularioPartida(forms.ModelForm):

    class Meta:
        # modelo usado para el formulario de Partida en la vista crear_partida
        model = Partida
        # el atributo de Partida que no quiero que aprezca en la view
        exclude = ('owner', 'mapa','jugador2', 'jugador3', 'jugador4', 'jugador5')
        
fields = '__all__'

