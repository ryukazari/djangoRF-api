from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Usuario,Libro,Prestamo
from .serializers import UsuarioSerializer, LibroSerializer, PrestamoSerializer, UsuarioMiniSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    #def predeterminada
    def list(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        serializer = UsuarioMiniSerializer(usuarios, many=True)
        return Response(serializer.data)

class LibroViewSet(viewsets.ModelViewSet):

    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class PrestamoViewSet(viewsets.ModelViewSet):

    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
