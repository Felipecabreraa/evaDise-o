from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Libro, Noticia, Usuario, Historial
from .forms import Libroform
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

    # Redirigir al usuario a la página de inicio de sesión o alguna otra página
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

def noticia_detalle(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render(request, 'noticia_detalle.html', {'noticia': noticia})

def login(request):
    return render(request,'login.html')

def iniciarSesion(request):
    # preguntar si estoy accediendo mediante el metodo POST
    if request.method == "POST":
        nom = request.POST["username"]    # recupere el valor ingresado en la casilla 
        pas = request.POST["password"]    # recupere el valor ingresado en la casilla 
        usuarioValidado = Usuario.objects.filter(nombre_usuario=nom, password_usuario=pas).values()
        # debo preguntar si lo encontro o no
        if usuarioValidado:
            # Ya que fue encontrado, vamos a registrar la accion en el Historial
            des = "EL USUARIO "+nom+" INICIO SESION"
            tbl = "HISTORIAL"
            fyh = datetime.now()
            idu = usuarioValidado[0]['id']
            his = Historial(descripcion_historial=des, tabla_afectada_historial=tbl, fecha_hora_historial=fyh,usuario_id=idu)
            his.save()
            # Vamos a crear las sesiones para el usuario
            request.session["nomUsuario"] = nom
            request.session["idUsuario"] = idu
            request.session["estadoUsuario"] = True
            
            # Configurar el tipo de usuario en la sesión
            if nom.upper() == "ADMIN":
                request.session["tipo_usuario"] = "admin"
            else:
                request.session["tipo_usuario"] = "operario"
            
            # Redirigir según el tipo de usuario
            if nom.upper() == "ADMIN":
                return render(request,"menu_admin.html")
            else:
                return render(request,"menu_usuario.html")

        else:
            # aqui debo enviar un error ya que no fue encontrado el usuario
            datos = {"error":"El Usuario no existe, intente nuevamente"}
            return render(request,"login.html",datos)

    else:
        # aqui debo enviar un error ya que esta intentando acceder de manera erronea.
        datos = {"error":"La Forma de acceder es incorrecta, debes logearte!"}
        return render(request,"login.html",datos)

    


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
