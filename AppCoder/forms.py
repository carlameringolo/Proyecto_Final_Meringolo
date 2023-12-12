from django import forms
from .models import *


class ContactoForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields=['nombre','mail','tel','comentario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'tu-clase-css'}),
            'mail': forms.EmailInput(attrs={'class': 'tu-clase-css'}),
            'tel': forms.TextInput(attrs={'class': 'tu-clase-css'}),
            'comentario': forms.Textarea(attrs={'class': 'tu-clase-css'}),
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['nombre','mail','tel','metodo_de_pago']


class ProductoForm(forms.ModelForm):
    class MEta:
        models=Producto
        fields=['nombre_producto','precio','imagen','empleado']

