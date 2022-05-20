from dataclasses import field
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView,ListView
from .models import Direccion,  Reserva, Vehiculo,Usuario
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.


#Nombre y clave para mapbox
token='mapbox_token'
key='pk.eyJ1Ijoid2F6b3dza2lkZXZlbG9wIiwiYSI6ImNrcTdneXZ4ejA2M2Uyd3VoY29hZTVjYXYifQ.wUjItHT_F5ZCMXUcwx5_xA'
parkings='lugares'

class PlaceView(CreateView):
    #Atributos del CRUD 
    model = Direccion
    fields = ['lugar']
    template_name = 'places/home.html'
    success_url = '/'
    placeObjects=Direccion.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[token] = key
        context[parkings] = Direccion.objects.all()
        return context

def inicio(request):
    return render(request, 'inicio.html', context={token:key, parkings:PlaceView.placeObjects},)


class UsuarioCreate(CreateView):
    
    model = Usuario
    template_name = 'admin_usuarios/usuario_form.html'
    fields = '__all__'
class UsuarioUpdate(UpdateView):
    model = Usuario
    template_name = 'admin_usuarios/usuario_form.html'
    fields = ['rut_user','pnombre','apaterno']

class UsuarioDelete(DeleteView):
    
    model = Usuario
    template_name = 'admin_usuarios/usuario_confirm_delete.html'
    success_url = reverse_lazy('inicio')

class UsuarioDetailView(DetailView):

    model = Usuario
    template_name = 'admin_usuarios/usuario_detail.html'

class UsuarioListView(ListView):

    model = Usuario
    template_name = 'admin_usuarios/usuario_list.html'
    paginate_by = 3

class ReservaCreate(CreateView):
    
    model = Reserva
    template_name = 'admin_reservas/reserva_form.html'
    fields = '__all__'
class ReservaUpdate(UpdateView):
    model = Reserva
    template_name = 'admin_reservas/reserva_form.html'
    fields = ['fecha','hora_desde','hora_hasta']

class ReservaDelete(DeleteView):
    
    model = Reserva
    template_name = 'admin_reservas/reserva_confirm_delete.html'
    success_url = reverse_lazy('inicio')

class ReservaDetailView(DetailView):

    model = Reserva
    template_name = 'admin_reservas/reserva_detail.html'

class ReservaListView(ListView):

    model = Reserva
    template_name = 'admin_reservas/reserva_list.html'
    paginate_by = 3