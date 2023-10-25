from django.contrib import admin
from .models import Libro
from .models import Noticia

# Register your models here.


admin.site.register(Libro)
admin.site.register(Noticia)