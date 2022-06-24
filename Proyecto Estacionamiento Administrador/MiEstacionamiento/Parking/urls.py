from django.urls import path
from .views import ModeloCreate, ModeloDelete, ModeloDetailView, ModeloUpdate, PlaceDelete, PlaceDetailView, PlaceModifyView, PlaceView, PuestoCreate, PuestoDelete, PuestoDetailView, PuestoUpdate, ReservaCreate, ReservaDelete, ReservaDetailView, ReservaListView, ReservaUpdate, SucursalCreate, SucursalDelete, SucursalDetailView, SucursalUpdate,  direccion_list,inicio,UsuarioUpdate,UsuarioDelete,UsuarioListView,UsuarioCreate,UsuarioDetailView, modelo_list, puesto_list, sucursal_list


urlpatterns = [
    path('home',PlaceView.as_view(),name='home'),
    path('',inicio,name='inicio'),
]

urlpatterns += [
    
    #Administracion de sucursales
    path('sucursal/create/', SucursalCreate.as_view(), name='sucursal_create'),
    path('sucursal/<str:pk>/', SucursalDetailView.as_view(), name='sucursal_detail'),
    path('sucursal/<str:pk>/update/', SucursalUpdate.as_view(),name='sucursal_update'),
    path('sucursal/<str:pk>/delete/', SucursalDelete.as_view(), name='sucursal_delete'),
    path('sucursal', sucursal_list, name="sucursal_list"),

    #Administracion de direcciones
    path('direccion/<int:pk>/update/', PlaceModifyView.as_view(), name='place_update'),
    path('direccion/<int:pk>/delete/', PlaceDelete.as_view(),name='place_delete'),
    path('direccion/<int:pk>/', PlaceDetailView.as_view(), name='place_detail'),
    path('listar', direccion_list, name="place_list"),

    #Administracion de usuarios
    path('usuario/create/', UsuarioCreate.as_view(), name='usuario_create'),
    path('usuario/<int:pk>/', UsuarioDetailView.as_view(), name='usuario_detail'),
    path('usuario/<int:pk>/update/', UsuarioUpdate.as_view(),name='usuario_update'),
    path('usuario/<int:pk>/delete/', UsuarioDelete.as_view(), name='usuario_delete'),
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),

    #Administracion de reservas
    path('reserva/create/', ReservaCreate.as_view(), name='reserva_create'),
    path('reserva/<str:pk>/', ReservaDetailView.as_view(), name='reserva_detail'),
    path('reserva/<str:pk>/update/', ReservaUpdate.as_view(),name='reserva_update'),
    path('reserva/<str:pk>/delete/', ReservaDelete.as_view(), name='reserva_delete'),
    path('reservas/', ReservaListView.as_view(), name='reserva_list'),

    #Administracion de puestos
    path('puesto/create/', PuestoCreate.as_view(), name='puesto_create'),
    path('puesto/<str:pk>/', PuestoDetailView.as_view(), name='puesto_detail'),
    path('puesto/<str:pk>/update/', PuestoUpdate.as_view(),name='puesto_update'),
    path('puesto/<str:pk>/delete/', PuestoDelete.as_view(), name='puesto_delete'),
    path('puesto', puesto_list, name="puesto_list"),

    #Administracion de puestos
    path('modelo/create/', ModeloCreate.as_view(), name='modelo_create'),
    path('modelo/<str:pk>/', ModeloDetailView.as_view(), name='modelo_detail'),
    path('modelo/<str:pk>/update/', ModeloUpdate.as_view(),name='modelo_update'),
    path('modelo/<str:pk>/delete/', ModeloDelete.as_view(), name='modelo_delete'),
    path('modelo', modelo_list, name="modelo_list"),
    

     

]