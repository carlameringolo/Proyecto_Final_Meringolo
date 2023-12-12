from django.shortcuts import render
from .forms import *

# Create your views here.
def inicio(req):
    return render(req,'inicio.html')

def contacto(req):
    formulario=ContactoForm()

    if req.method=='POST':
        formulario=ContactoForm(req.POST)
        if formulario.is_valid():
            formulario.save()
            return render(req,'inicio.html',{'mensaje':'Mensaje enviado con exito'})
    return render(req,'contacto.html',{'formulario':formulario})
 
