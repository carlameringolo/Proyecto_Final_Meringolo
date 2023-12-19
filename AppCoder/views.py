from django.shortcuts import render, redirect
from .forms import *
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotAllowed


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
                return render(req, 'contacto.html', {'mensaje': 'Mensaje enviado con exito'})
            except:
                return render(req, 'contacto.html', {'mensaje': 'Error al enviar mensaje'})
        else:
            return render(req, 'contacto.html', {'mensaje': 'Formulario invalido'})
    return render(req,'contacto.html',{'formulario':formulario})
 

class ClienteList(LoginRequiredMixin,ListView):
    model=Cliente
    template_name='cliente_list.html'
    context_object_name='cliente'
    queryset=Cliente.objects.all()
    login_url='Login'


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





#login, logout
def loginView(req):

    if req.user.is_authenticated:
        return render(req, 'inicio.html', {'mensaje': 'Ya hay un usuario logeado. Por favor dirigite al logout'})

    if req.method=='POST':
        formulario=AuthenticationForm(req,data=req.POST)

        if formulario.is_valid():

            data=formulario.cleaned_data
            usuario=data['username']
            psw=data['password']
            user=authenticate(username=usuario,password=psw)

            if user:
                login(req,user)
                return render(req, 'inicio.html', {'mensaje': f'Bienvenido {usuario}!'})     
            else:
                return render(req, 'inicio.html', {'mensaje': f'Datos incorrectos'})
    else:
        formulario=AuthenticationForm()
    
    return render(req, 'login.html',{'formulario':formulario})


def logoutView(req):
    if req.user.is_authenticated:
        logout(req)
        return render(req, 'inicio.html', {'mensaje': 'Has cerrado sesion. Vuela pronto!'})     
        
    else:
        return render(req, 'inicio.html', {'mensaje': 'No hay ningun usuario logeado'})     



def verificarLogin(req):
    user=req.user
    if user.is_authenticated:
        return user
    return None



def register(req):
    if req.method=='POST':
        formulario=UserCreationForm(req.POST)

        if formulario.is_valid():
            user=formulario.save()

            Empleado.objects.create(user=user)
            loginView(req)
            return render(req,'inicio.html')
    
    else:
        formulario=UserCreationForm()
    return render(req,'registro.html',{'formulario':formulario})






@login_required(login_url='Login')
def agregar_producto(req):

    if req.method=='POST':

        formulario=ProductoForm(req.POST, req.FILES)

        if formulario.is_valid():

            data=formulario.cleaned_data

            producto=Producto(user=req.user, imagen=data['imagen'])
            producto.save()            

            return render(req,'inicio.html',{'mensaje':'Imagen actualizados con exito'})

    else:
        formulario=ProductoForm()
    
        return render(req,'agregarProducto.html',{'formulario':formulario})






class ProductoCreate(LoginRequiredMixin,CreateView):
    model=Producto
    template_name='producto_create.html'
    fields=['nombre_producto','precio','imagen','empleado']
    success_url='/app-coder/listaProductos'
    login_url='Login'

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
    login_url='Login'


def buscarProducto(req):
    if req.method=='GET' or req.method=='POST':
        formulario=BusquedaForm(req.GET if req.method=='GET' else req.POST)
        if formulario.is_valid():
            query=req.GET['nombre_producto']
            try:
                producto=Producto.objects.get(nombre_producto__icontains=query)
                return render(req, 'producto_detail.html', {'producto':producto})
            except Producto.DoesNotExist:
                return render(req,'productoNo_encontrado.html', {'mensaje':'Producto no encontrado'})
        else:
            return render(req,'buscar_producto.html',{'formulario':formulario})
    else:
        return HttpResponseNotAllowed(['GET','POST'])
   




@login_required(login_url='Login')
def editar_perfil(req):
    
    usuario= req.user

    if req.method == 'POST':
        
        formulario=UserEditForm(req.POST,instance=req.user)
        
        if formulario.is_valid():

            data=formulario.cleaned_data

            usuario.first_name=data['first_name']
            usuario.last_name=data['last_name']
            usuario.email=data['email']
            usuario.save()

            context={
                'first_name':usuario.first_name,
                'last_name':usuario.last_name,
                'email':usuario.email
            }

            return render(req,'perfil_actualizado.html',context)

    else:
        formulario=UserEditForm()

    if not req.user.is_authenticated:
        return render(req, 'login.html',{'formulario':formulario})
    
    return render(req, 'editarPerfil.html',{'formulario':formulario})




def tablaPagos(req):
    return render(req,'tabla.html')


