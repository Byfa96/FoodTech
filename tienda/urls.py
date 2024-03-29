from django.contrib import admin
from django.urls import path
from .views import (mostrar_inicio, 
                    mostrar_registro, 
                    mostrar_producto,
                    mostrar_login, 
                    salir, 
                    carro,
                    listar_producto,
                    crear_producto,
                    eliminar_producto,
                    editar_producto,
                    crear_inventario,
                    borrar_carro,
                    borrar_todo_carro)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', mostrar_inicio, name='inicio'),
    #Login y registro
    path('registro/', mostrar_registro, name='registro'),
    path('inicio_sesion/', mostrar_login, name='login'),
    path('salir/', salir, name='salir'),
    path('carro/', carro, name='carro'),
    path('producto/', mostrar_producto, name='producto'),
    path('listar_producto/', listar_producto, name='listar_producto' ),
    #
    path('crear-inv/',crear_inventario, name = 'crear-invntario'),
    path('borrar/', borrar_carro,name = 'borrar'),
    path('borrar-todo/', borrar_todo_carro,name = 'borrartodo'),
    #
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:producto_id>/', editar_producto, name='editar_producto'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)