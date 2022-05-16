from django import forms
from django.forms import ModelForm
from .models import *

#creamos un tetmplate del formulario
class ProductoForm(ModelForm):
    
    #validar que los campos sean limitados
    # nombre = forms.CharField(min_length=10,max_length=20)
    # precio = forms.IntegerField(min_value=400)

    class Meta:
        model = Producto
        fields = ['plu_codigo','nombre','marca','precio','stock','tipo','imagen']

      
