from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name="nosotros"),
    path('index', views.index, name="index"),
    path('crear', views.crear, name="crear"),
    path('editar', views.editar, name="editar"),
    path('eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('editar/<int:id>', views.editar, name="editar"),
    path('noticias/<int:noticia_id>/', views.noticia_detalle, name='detalle_noticia'),
    path('login', views.login, name="login"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
