from __future__ import unicode_literals

from django.contrib import admin
from .models import Pieza, Mapa, Partida

# Register your models here.

admin.site.register(Pieza)
admin.site.register(Mapa)
admin.site.register(Partida)

