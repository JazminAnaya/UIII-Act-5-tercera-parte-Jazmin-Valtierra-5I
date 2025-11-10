# app_Cinepolis/admin.py
from django.contrib import admin
from .models import Sucursal, Sala, Pelicula

# Registra tus modelos aquí
admin.site.register(Sucursal)
admin.site.register(Sala)
admin.site.register(Pelicula) 