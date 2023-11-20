
from django import forms
from .models import Libro

class Libroform(forms.ModelForm):
    class Meta:
        model = Libro
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(Libroform, self).__init__(*args, **kwargs)

        # Configurar mensajes de error personalizados
        self.fields['titulo'].error_messages = {'required': 'Este campo es obligatorio.'}
        self.fields['imagen'].error_messages = {'required': 'Por favor, sube una imagen.'}
        self.fields['descripcion'].error_messages = {'required': 'Por favor, añade una descripcion.'}

        # Continúa con otros campos según sea necesario
