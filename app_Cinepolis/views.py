
# app_Cinepolis/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Sucursal, Sala, Pelicula # Asegúrate de importar Pelicula
from datetime import datetime

# Función para la página de inicio
def inicio_cinepolis(request):
    return render(request, 'inicio.html')

# Función para agregar una sucursal
def agregar_sucursal(request):
    if request.method == 'POST':
        nombre_cine = request.POST.get('nombre_cine')
        direccion = request.POST.get('direccion')
        ciudad = request.POST.get('ciudad')
        telefono = request.POST.get('telefono')
        numero_salas = request.POST.get('numero_salas')
        estado = request.POST.get('estado')
        formatos = request.POST.get('formatos')

        Sucursal.objects.create(
            nombre_cine=nombre_cine,
            direccion=direccion,
            ciudad=ciudad,
            telefono=telefono,
            numero_salas=numero_salas,
            estado=estado,
            formatos=formatos
        )
        return redirect('ver_sucursales')
    return render(request, 'sucursal/agregar_sucursal.html')

# Función para ver todas las sucursales
def ver_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/ver_sucursales.html', {'sucursales': sucursales})

# Función para mostrar el formulario de actualización de una sucursal
def actualizar_sucursal(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': sucursal})

# Función para realizar la actualización de una sucursal
def realizar_actualizacion_sucursal(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == 'POST':
        sucursal.nombre_cine = request.POST.get('nombre_cine')
        sucursal.direccion = request.POST.get('direccion')
        sucursal.ciudad = request.POST.get('ciudad')
        sucursal.telefono = request.POST.get('telefono')
        sucursal.numero_salas = request.POST.get('numero_salas')
        sucursal.estado = request.POST.get('estado')
        sucursal.formatos = request.POST.get('formatos')
        sucursal.save()
        return redirect('ver_sucursales')
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': sucursal})


# Función para borrar una sucursal
def borrar_sucursal(request, pk):
    sucursal = get_object_or_404(Sucursal, pk=pk)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('ver_sucursales')
    return render(request, 'sucursal/borrar_sucursal.html', {'sucursal': sucursal})


# Función para agregar una sala
def agregar_sala(request):
    sucursales = Sucursal.objects.all() # Necesitamos las sucursales para el dropdown
    if request.method == 'POST':
        numero_sala = request.POST.get('numero_sala')
        tipo_sala = request.POST.get('tipo_sala')
        capacidad = request.POST.get('capacidad')
        estado = request.POST.get('estado')
        fecha_ultimo_mantenimiento_str = request.POST.get('fecha_ultimo_mantenimiento')
        asientos_especiales = request.POST.get('asientos_especiales')
        sucursal_id = request.POST.get('sucursal')

        sucursal_obj = get_object_or_404(Sucursal, pk=sucursal_id)
        fecha_mantenimiento = datetime.strptime(fecha_ultimo_mantenimiento_str, '%Y-%m-%d').date()

        Sala.objects.create(
            numero_sala=numero_sala,
            tipo_sala=tipo_sala,
            capacidad=capacidad,
            estado=estado,
            fecha_ultimo_mantenimiento=fecha_mantenimiento,
            asientos_especiales=asientos_especiales,
            sucursal=sucursal_obj
        )
        return redirect('ver_salas')
    return render(request, 'sala/agregar_sala.html', {'sucursales': sucursales})

# Función para ver todas las salas
def ver_salas(request):
    salas = Sala.objects.all().select_related('sucursal').order_by('sucursal__nombre_cine', 'numero_sala')
    return render(request, 'sala/ver_salas.html', {'salas': salas})

# Función para mostrar el formulario de actualización de una sala
def actualizar_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    sucursales = Sucursal.objects.all()
    return render(request, 'sala/actualizar_sala.html', {'sala': sala, 'sucursales': sucursales})

# Función para realizar la actualización de una sala
def realizar_actualizacion_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    if request.method == 'POST':
        sala.numero_sala = request.POST.get('numero_sala')
        sala.tipo_sala = request.POST.get('tipo_sala')
        sala.capacidad = request.POST.get('capacidad')
        sala.estado = request.POST.get('estado')
        fecha_ultimo_mantenimiento_str = request.POST.get('fecha_ultimo_mantenimiento')
        sala.fecha_ultimo_mantenimiento = datetime.strptime(fecha_ultimo_mantenimiento_str, '%Y-%m-%d').date()
        sala.asientos_especiales = request.POST.get('asientos_especiales')
        sucursal_id = request.POST.get('sucursal')
        sala.sucursal = get_object_or_404(Sucursal, pk=sucursal_id)
        sala.save()
        return redirect('ver_salas')
    return render(request, 'sala/actualizar_sala.html', {'sala': sala, 'sucursales': Sucursal.objects.all()})

# Función para borrar una sala
def borrar_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    if request.method == 'POST':
        sala.delete()
        return redirect('ver_salas')
    return render(request, 'sala/borrar_sala.html', {'sala': sala})

# Función para agregar una película
def agregar_pelicula(request):
    salas = Sala.objects.all().select_related('sucursal').order_by('sucursal__nombre_cine', 'numero_sala')
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        genero = request.POST.get('genero')
        clasificacion = request.POST.get('clasificacion')
        duracion = request.POST.get('duracion')
        sinopsis = request.POST.get('sinopsis')
        director = request.POST.get('director')
        salas_seleccionadas_ids = request.POST.getlist('salas') # Obtener una lista de IDs

        pelicula = Pelicula.objects.create(
            titulo=titulo,
            genero=genero,
            clasificacion=clasificacion,
            duracion=duracion,
            sinopsis=sinopsis,
            director=director
        )
        # Asignar salas a la película
        if salas_seleccionadas_ids:
            pelicula.salas.set(salas_seleccionadas_ids) # Usa .set() para ManyToMany

        return redirect('ver_peliculas')
    return render(request, 'pelicula/agregar_pelicula.html', {'salas': salas})

# Función para ver todas las películas
def ver_peliculas(request):
    peliculas = Pelicula.objects.all().prefetch_related('salas__sucursal')
    return render(request, 'pelicula/ver_peliculas.html', {'peliculas': peliculas})

# Función para mostrar el formulario de actualización de una película
def actualizar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    salas = Sala.objects.all().select_related('sucursal').order_by('sucursal__nombre_cine', 'numero_sala')
    salas_asignadas_ids = pelicula.salas.values_list('id_sala', flat=True) # Obtener IDs de salas ya asignadas

    return render(request, 'pelicula/actualizar_pelicula.html', {
        'pelicula': pelicula,
        'salas': salas,
        'salas_asignadas_ids': list(salas_asignadas_ids)
    })

# Función para realizar la actualización de una película
def realizar_actualizacion_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        pelicula.titulo = request.POST.get('titulo')
        pelicula.genero = request.POST.get('genero')
        pelicula.clasificacion = request.POST.get('clasificacion')
        pelicula.duracion = request.POST.get('duracion')
        pelicula.sinopsis = request.POST.get('sinopsis')
        pelicula.director = request.POST.get('director')
        pelicula.save()

        salas_seleccionadas_ids = request.POST.getlist('salas')
        pelicula.salas.set(salas_seleccionadas_ids) # Actualiza las salas asociadas

        return redirect('ver_peliculas')
    return render(request, 'pelicula/actualizar_pelicula.html', {'pelicula': pelicula, 'salas': Sala.objects.all()})

# Función para borrar una película
def borrar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        pelicula.delete()
        return redirect('ver_peliculas')
    return render(request, 'pelicula/borrar_pelicula.html', {'pelicula': pelicula})