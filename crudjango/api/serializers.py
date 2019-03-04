#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from crudjango.api.models import Usuario, Libro, Prestamo


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('dni', 'nombre', 'direccion', 'telefono', 'email', 'ocupacion')

class UsuarioMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('dni', 'nombre')


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id', 'titulo', 'autor', 'editorial')

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ('id', 'fechaEntrega', 'fechaDevolucion', 'usuario', 'libro')

