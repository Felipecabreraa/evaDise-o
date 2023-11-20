from django import forms
from .models import Libro

class Libroform(forms.ModelForm):
    class Meta:
        model = Libro
        fields ='__all__'
        
        
        
        

