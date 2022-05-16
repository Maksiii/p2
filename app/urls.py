from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name="index" ),
    path('index_sesion_iniciada/', index_sesion_iniciada,name="index_sesion_iniciada" ),
    path('segumiento_de_compra/', segumiento_de_compra,name="segumiento_de_compra" ),
    path('historial/', historial,name="historial" ),
    path('carrito/', carrito,name="carrito" ),
    path('agregarproducto/', agregarproducto,name="agregarproducto" ),
    path('modificarProductos/<plu_codigo>/', modificarProductos,name="modificarProductos" ),
    path('eliminarProducto/<plu_codigo>/', eliminarProducto,name="eliminarProducto" ),
    path('listarProductos/', listarProductos,name="listarProductos" ),
    path('comprado/', comprado,name="comprado" ),
    path('crear_usuario/', crear_usuario,name="crear_usuario" ),
    path('crea_usu/', crea_usu,name="crea_usu" ),

]

