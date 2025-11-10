# app_Cinepolis/models.py
from django.db import models

# ===================
# MODELO: Sucursal
# ===================
class Sucursal(models.Model):
    ESTADOS = [
        ('activo', 'Activo'),
        ('cerrado', 'Cerrado'),
        ('mantenimiento', 'Mantenimiento'),
    ]
    FORMATOS = [
        ('tradicional', 'Tradicional'),
        ('3D', '3D'),
        ('4DX', '4DX'),
        ('VIP', 'VIP'),
        ('IMAX', 'IMAX'),
        ('JUNIOR', 'Junior'),
    ]
    id_sucursal = models.AutoField(primary_key=True)
    nombre_cine = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    numero_salas = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activo')
    formatos = models.CharField(max_length=20, choices=FORMATOS, default='tradicional')

    def __str__(self):
        return f"{self.nombre_cine} - {self.ciudad}"

# ============================================
# MODELO: Sala
# ============================================
class Sala(models.Model):
    TIPOS_SALA = [
        ('Tradicional', 'Tradicional'),
        ('3D', '3D'),
        ('4DX', '4DX'),
        ('VIP', 'VIP'),
        ('IMAX', 'IMAX'),
        ('JUNIOR', 'Junior'),
    ]
    ESTADOS_SALA = [
        ('Ocupada', 'Ocupada'),
        ('Desocupada', 'Desocupada'),
        ('En mantenimiento', 'En mantenimiento'),
    ]
    id_sala = models.AutoField(primary_key=True)
    numero_sala = models.IntegerField()
    tipo_sala = models.CharField(max_length=20, choices=TIPOS_SALA, default='Tradicional')
    capacidad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS_SALA, default='Desocupada')
    fecha_ultimo_mantenimiento = models.DateField()
    asientos_especiales = models.IntegerField()

    # Relación 1 a muchos: una sucursal puede tener muchas salas
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='salas')

    def __str__(self):
        return f"Sala {self.numero_sala} - {self.tipo_sala} ({self.sucursal.nombre_cine})"

# ============================================
# MODELO: Pelicula
# ============================================
class Pelicula(models.Model):
    id_pelicula = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    clasificacion = models.CharField(max_length=100)
    duracion = models.IntegerField(help_text="Duración en minutos")
    sinopsis = models.TextField()
    director = models.CharField(max_length=150)

    # Relación muchos a muchos: una sala puede tener varias películas y viceversa
    salas = models.ManyToManyField(Sala, related_name='peliculas')

    def __str__(self):
        return self.titulo