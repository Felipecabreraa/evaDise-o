from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Libro, Noticia
from .forms import Libroform

# Create your views here.

def inicio(request):
    noticias = Noticia.objects.all()
    return render(request, 'inicio.html', {'noticias': noticias})

def nosotros(request):
    return render(request, 'nosotros.html')

def index(request):
    libros = Libro.objects.all()
    return render(request,'index.html', {'libros':libros})

def crear(request):
    formulario = Libroform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, 'crear.html', {'formulario': formulario})

def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = Libroform(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('index')
    return render(request, 'editar.html', {'formulario':formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('index')
    return render(request, 'eliminar.html')

def noticia_detalle(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render(request, 'noticia_detalle.html', {'noticia': noticia})

