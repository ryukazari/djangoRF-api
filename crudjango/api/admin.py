from django.contrib import admin
from crudjango.api.models import Usuario, Libro, Prestamo
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Prestamo)