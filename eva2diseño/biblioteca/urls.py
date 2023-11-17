from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.login, name='login'),
    path('inicio', views.inicio, name='inicio'),
    path('login', views.iniciarSesion),
    path('logout', views.cerrarSesion, name='logout'),
    path('nosotros', views.nosotros, name="nosotros"),
    path('index', views.index, name="index"),
    path('crear', views.crear, name="crear"),
    path('editar', views.editar, name="editar"),
    path('eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('editar/<int:id>', views.editar, name="editar"),
    path('noticias/<int:noticia_id>/', views.noticia_detalle, name='detalle_noticia'),
    path('login', views.login, name="login"),
    path('menu_usuario', views.mostrarMenuUsuario, name="menu_usuario"),
    path('menu_admin', views.mostrarMenuAdmin, name="menu_admin"),
    path('listar_historial', views.mostrarListarHistorial),





    



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
