from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

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
    class Meta:
        model=Producto
        fields=['nombre_producto','precio','imagen','empleado']



class BusquedaForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['nombre_producto',]




class UserEditForm(UserChangeForm):
    password=forms.CharField(
        help_text='',
        widget=forms.HiddenInput(),required=False
    )

    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['email','first_name','last_name','password1','password2']

    def clean_password2(self):

        print(self.cleaned_data)

        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2 
    

