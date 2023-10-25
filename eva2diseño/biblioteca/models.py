from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    descripcion =models.TextField(verbose_name="descripcion", null=True)
    
    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.descripcion
        return fila 
    
    def delete(self, using=None, keep_parents=False ):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
        
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='static/')  # Supongamos que las imágenes de noticias se suben a la carpeta 'noticias/'

    def __str__(self):
        return self.titulo
   