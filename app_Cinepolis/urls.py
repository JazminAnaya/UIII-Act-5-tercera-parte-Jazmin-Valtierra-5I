# app_Cinepolis/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_cinepolis, name='inicio_cinepolis'),

    # Rutas para Sucursales
    path('sucursales/agregar/', views.agregar_sucursal, name='agregar_sucursal'),
    path('sucursales/', views.ver_sucursales, name='ver_sucursales'),
    path('sucursales/actualizar/<int:pk>/', views.actualizar_sucursal, name='actualizar_sucursal'),
    path('sucursales/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_sucursal, name='realizar_actualizacion_sucursal'),
    path('sucursales/borrar/<int:pk>/', views.borrar_sucursal, name='borrar_sucursal'),

    # Rutas para Salas
    path('salas/agregar/', views.agregar_sala, name='agregar_sala'),
    path('salas/', views.ver_salas, name='ver_salas'),
    path('salas/actualizar/<int:pk>/', views.actualizar_sala, name='actualizar_sala'),
    path('salas/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_sala, name='realizar_actualizacion_sala'),
    path('salas/borrar/<int:pk>/', views.borrar_sala, name='borrar_sala'),

    # Rutas para Películas (¡Nuevas!)
    path('peliculas/agregar/', views.agregar_pelicula, name='agregar_pelicula'),
    path('peliculas/', views.ver_peliculas, name='ver_peliculas'),
    path('peliculas/actualizar/<int:pk>/', views.actualizar_pelicula, name='actualizar_pelicula'),
    path('peliculas/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_pelicula, name='realizar_actualizacion_pelicula'),
    path('peliculas/borrar/<int:pk>/', views.borrar_pelicula, name='borrar_pelicula'),
]