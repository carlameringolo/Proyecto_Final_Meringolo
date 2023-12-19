from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('contacto',contacto,name='Contacto'),

    path('listaClientes/', ClienteList.as_view(), name='ListarClientes'),
    path('detalleCliente/<pk>', ClienteDetail.as_view(), name='DetalleCliente'),
    path('crearCliente/', ClienteCreate.as_view(), name='CrearCliente'),
    path('actualizarCliente/<pk>', ClienteUpdate.as_view(), name='ActualizarCliente'),
    path('eliminarCliente/<pk>', ClienteDelete.as_view(), name='EliminarCliente'),

    path('detalleProducto/<pk>', ProductoDetail.as_view(), name='DetalleProducto'),
    path('actualizarProducto/<pk>', ProductoUpdate.as_view(), name='ActualizarProducto'),
    path('eliminarProducto/<pk>', ProductoDelete.as_view(), name='EliminarProducto'),

    path('listaProductos', ProductoList.as_view(), name='ListarProductos'),

    path('crearProducto', ProductoCreate.as_view(), name='CrearProducto'),
    path('agregar-producto', agregar_producto, name='AgregarProducto'),


    path('accounts/login', loginView, name='Login'),
    path('logout', logoutView, name='Logout'),
    path('registrar', register, name='Registrar'),

    path('buscarProducto', buscarProducto, name='BuscarProducto'),

    path('editarPerfil',editar_perfil,name='EditarPerfil'),
    path('tabla-pagos',tablaPagos,name='TablaPagos')

 
]
