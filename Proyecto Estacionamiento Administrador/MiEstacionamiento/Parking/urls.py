from django.urls import path
from .views import PlaceView, ReservaCreate, ReservaDelete, ReservaDetailView, ReservaListView, ReservaUpdate,inicio,UsuarioUpdate,UsuarioDelete,UsuarioListView,UsuarioCreate,UsuarioDetailView


urlpatterns = [
    path('home',PlaceView.as_view(),name='home'),
    path('',inicio,name='inicio'),
]

urlpatterns += [
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

]