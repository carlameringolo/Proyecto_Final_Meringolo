from django.shortcuts import render
from .forms import *
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def inicio(req):
    return render(req,'inicio.html')



def contacto(req):
    formulario=ContactoForm()

    if req.method=='POST':
        formulario=ContactoForm(req.POST)
        if formulario.is_valid():
            try:
                formulario.save()
                messages.succes(req,'Mensaje enviado con exito')
            except:
                messages.error(req,'Error al enviar mensaje')
        else:
            messages.error(req,'Formulario invalido')
    return render(req,'contacto.html',{'formulario':formulario})
 

class ClienteList(ListView):
    model=Cliente
    template_name='cliente_list.html'
    context_object_name='cliente'
    queryset=Cliente.objects.all()


class ClienteDetail(DetailView):
    model=Cliente
    template_name='cliente_detail.html'
    context_object_name='cliente'

class ClienteCreate(CreateView):
    model=Cliente
    template_name='cliente_create.html'
    fields=['nombre','mail','tel','metodo_de_pago']
    success_url='/app-coder/listaClientes'
     
class ClienteUpdate(UpdateView):
    model=Cliente
    template_name='cliente_update.html'
    fields=('__all__')
    success_url='/app-coder/listaClientes'
    context_object_name='cliente'

class ClienteDelete(DeleteView):
    model=Cliente
    template_name='cliente_delete.html'
    success_url='/app-coder/listaClientes'
    context_object_name='cliente'



@login_required
def agregar_producto(req):

    empleado=req.user.empleado

    if not empleado:
        return render(req,'login.html')
    
    if req.method=='POST':

        formulario=ProductoForm(req.POST, req.FILES)

        if formulario.is_valid():

            producto=formulario.save(commit=False)
            producto.empleado=empleado
            producto.save()

            messages.succes(req,'Producto agregado')

            return render(req,'producto_list.html')
        else:
            formulario=ProductoForm()
        
        return render(req,'agregarProducto.html',{'formulario':formulario})




class ProductoList(ListView):
    model=Producto
    template_name='producto_list.html'
    context_object_name='producto'

class ProductoDetail(DetailView):
    model=Producto
    template_name='producto_detail.html'
    context_object_name='producto'

     
class ProductoUpdate(UpdateView):
    model=Producto
    template_name='producto_update.html'
    fields=('__all__')
    success_url='/app-coder/listaProductos'
    context_object_name='producto'

class ProductoDelete(DeleteView):
    model=Producto
    template_name='producto_delete.html'
    success_url='/app-coder/listaProductos'
    context_object_name='producto'


