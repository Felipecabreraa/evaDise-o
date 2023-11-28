
from django import forms
from .models import Libro, Prestamo


class Libroform(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Libroform, self).__init__(*args, **kwargs)

        # Mensajes de error personalizados para los campos existentes
        self.fields['titulo'].error_messages = {'required': 'Este campo es obligatorio.'}
        self.fields['imagen'].error_messages = {'required': 'Por favor, sube una imagen.'}
        self.fields['descripcion'].error_messages = {'required': 'Por favor, añade una descripcion.'}

        # Mensajes de error personalizados para los nuevos campos
        self.fields['año_publicacion'].error_messages = {'required': 'Por favor, especifica el año de publicación.'}
        self.fields['categoria'].error_messages = {'required': 'Por favor, especifica una categoría.'}
        self.fields['autor'].error_messages = {'required': 'Por favor, indica el autor del libro.'}
        self.fields['editorial'].error_messages = {'required': 'Por favor, indica la editorial.'}


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libros', 'fecha_devolucion_estimada']  # Cambio de 'libro' a 'libros'

    fecha_devolucion_estimada = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Fecha de Entrega')