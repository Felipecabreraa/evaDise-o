from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Libro, Noticia, Usuario, Historial
from .forms import Libroform
from django.contrib import messages


from datetime import datetime
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

def inicio(request):
    noticias = Noticia.objects.all()
    return render(request, 'inicio.html', {'noticias': noticias})

def cerrarSesion(request):
    # Limpiar las variables de sesión
    if 'nomUsuario' in request.session:
        del request.session['nomUsuario']
    if 'estadoUsuario' in request.session:
        del request.session['estadoUsuario']
    if 'idUsuario' in request.session:
        del request.session['idUsuario']

    # Cerrar la sesión de Django
    logout(request)

    # Limpiar todos los mensajes
    list(messages.get_messages(request))

    # Redirigir al usuario a la página de inicio de sesión
    return redirect('login')

def nosotros(request):
    return render(request, 'nosotros.html')

def mostrarMenuAdmin(request):
    return render(request, 'menu_admin.html')



def mostrarMenuUsuario(request):
    return render(request, 'menu_usuario.html')


def index(request):
    libros = Libro.objects.all()
    return render(request,'index.html', {'libros':libros})

def crear(request):
    formulario = Libroform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Libro creado con éxito.')
        return redirect('index')
    else:
        messages.error(request, 'Error al crear el libro.')
    
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

def noticia_detalle(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render(request, 'noticia_detalle.html', {'noticia': noticia})

def login(request):
    return render(request,'login.html')

def iniciarSesion(request):
    if request.method == "POST":
        nom = request.POST.get("username")
        pas = request.POST.get("password")
        usuarioValidado = Usuario.objects.filter(nombre_usuario=nom, password_usuario=pas).first()

        if usuarioValidado:
            # Registro en el Historial
            des = f"EL USUARIO {nom} INICIÓ SESIÓN"
            tbl = "HISTORIAL"
            fyh = datetime.now()
            his = Historial(descripcion_historial=des, tabla_afectada_historial=tbl, fecha_hora_historial=fyh, usuario=usuarioValidado)
            his.save()

            # Creación de sesiones para el usuario
            request.session["nomUsuario"] = nom
            request.session["idUsuario"] = usuarioValidado.id
            request.session["estadoUsuario"] = True
            
            # Configuración del tipo de usuario en la sesión
            tipo_usuario = "admin" if nom.upper() == "ADMIN" else "operario"
            request.session["tipo_usuario"] = tipo_usuario

            # Añadir mensaje de éxito y contexto para redirección
            messages.success(request, 'Inicio de sesión exitoso.')
            context = {'redirect_url': 'menu_admin' if tipo_usuario == "admin" else 'menu_usuario'}
            return render(request, "login.html", context)
        else:
            # Añadir mensaje de error
            messages.error(request, 'El usuario no existe o la contraseña es incorrecta.')
    
    return render(request, "login.html")


def mostrarperfil_operador(request):
    return render(request, 'perfil_operador.html')


def mostrarperfil_administrador(request):
    return render(request, 'perfil_admin.html')



def mostrarListarHistorial(request):
    try:
        #Recuperar el valor de las sesiones
        nom = request.session["nomUsuario"]
        idu = request.session["idUsuario"]
        est = request.session["estadoUsuario"]
        if est is True:    # Pregunto si el usuario esta logeado
            if nom.upper() == "ADMIN":
                #historial = Historial.objects.all().values()
                historial = Historial.objects.select_related('usuario').all().order_by("-fecha_hora_historial")
                datos = {
                    "nomUsuario":request.session["nomUsuario"],
                    "historial":historial
                }
                return render(request,"listar_historial.html",datos)
            else:
                # si desean eliminen las sesiones creadas
                datos = {
                    "error":"Sin Privilegios, no puedes acceder"
                }      
                return render(request,"index.html",datos)
        else:
            datos = {
                    "error":"Error de Acceso, debes logearte para acceder a la plataforma"
            }      
            return render(request,"index.html",datos)
    except:
        datos = {
                    "error":"Error, debes logearte para acceder a la Plataforma"
        }
        return render(request, "index.html", datos)  
    

def inicio(request):
    # Verificar si el usuario ha iniciado sesión
    if 'nomUsuario' in request.session:
        nom = request.session['nomUsuario']
        
        # Determinar el tipo de usuario (admin o usuario normal)
        tipo_usuario = "admin" if nom.upper() == "ADMIN" else "OPERADOR"
        
        # Almacenar el tipo de usuario en la sesión
        request.session['tipo_usuario'] = tipo_usuario
    
    # Obtener las noticias u otros datos que desees mostrar en la página de inicio
    noticias = Noticia.objects.all()
    
    return render(request, 'inicio.html')

