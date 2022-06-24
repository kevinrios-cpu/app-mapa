from dataclasses import field
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView,ListView
from .models import Direccion, Modelo, Puesto, Reserva, Vehiculo, Usuario, SucursalEst 
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.


#Nombre y clave para mapbox
token='mapbox_token'
key='pk.eyJ1Ijoid2F6b3dza2lkZXZlbG9wIiwiYSI6ImNrcTdneXZ4ejA2M2Uyd3VoY29hZTVjYXYifQ.wUjItHT_F5ZCMXUcwx5_xA'
parkings='lugares'


class SucursalCreate(CreateView):
    
    model = SucursalEst
    template_name = 'admin_sucursales/sucursal_form.html'
    fields = '__all__'
class SucursalUpdate(UpdateView):
    model = SucursalEst
    template_name = 'admin_sucursales/sucursal_form.html'
    fields = ['id_suc','direccion_lugar','nom_sucursal', 'fono_suc', 'admin']

class SucursalDelete(DeleteView):
    
    model = SucursalEst
    template_name = 'admin_sucursales/sucursal_confirm_delete.html'
    success_url = reverse_lazy('inicio')

class SucursalDetailView(DetailView):

    model = SucursalEst
    template_name = 'admin_sucursales/sucursal_detail.html'

def sucursal_list(request):
    sucursal = SucursalEst.objects.all()
    contexto = {'sucursales':sucursal}
    return render(request, 'admin_sucursales/sucursal_list.html', contexto)


################################################################################

class PlaceView(CreateView):
    #Atributos del CRUD 
    model = Direccion
    fields = ['lugar']
    template_name = 'places/home.html'
    success_url = 'home'
    placeObjects=Direccion.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[token] = key
        context[parkings] = Direccion.objects.all()
        return context

class PlaceDelete(DeleteView):
    
    model = Direccion
    template_name = 'places/place_confirm_delete.html'
    success_url = reverse_lazy('inicio')
class PlaceModifyView(UpdateView):
    #Atributos del CRUD 
    model = Direccion
    fields = ['lugar']
    template_name = 'places/place_form.html'
    success_url = 'home'

class PlaceDetailView(DetailView):

    model = Direccion
    template_name = 'places/place_detail.html'


def direccion_list(request):
    direccion = Direccion.objects.all()
    contexto = {'places':direccion}
    return render(request, 'places/place_list.html', contexto)

def inicio(request):
    return render(request, 'sign_in.html', context={token:key, parkings:PlaceView.placeObjects},)

#######################################################################


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



#####################################################################

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




##############################################################################

class PuestoCreate(CreateView):
    
    model = Puesto
    template_name = 'admin_puestos/puesto_form.html'
    fields = '__all__'
class PuestoUpdate(UpdateView):
    model = Puesto
    template_name = 'admin_puestos/puesto_form.html'
    fields = ['id_puesto','letra_puesto','num_puesto', 'sucursal_est']

class PuestoDelete(DeleteView):
    
    model = Puesto
    template_name = 'admin_puestos/puesto_confirm_delete.html'
    success_url = reverse_lazy('inicio')

class PuestoDetailView(DetailView):

    model = Puesto
    template_name = 'admin_puestos/puesto_detail.html'

def puesto_list(request):
    puesto = Puesto.objects.all()
    contexto = {'puestos':puesto}
    return render(request, 'admin_puestos/puesto_list.html', contexto)


##############################################################################

class ModeloCreate(CreateView):
    
    model = Modelo
    template_name = 'admin_modelos/modelo_form.html'
    fields = '__all__'
class ModeloUpdate(UpdateView):
    model = Modelo
    template_name = 'admin_modelos/modelo_form.html'
    fields = ['id_modelo','letra_puesto','num_puesto', 'sucursal_est']

class ModeloDelete(DeleteView):
    
    model = Modelo
    template_name = 'admin_modelos/modelo_confirm_delete.html'
    success_url = reverse_lazy('inicio')

class ModeloDetailView(DetailView):

    model = Modelo
    template_name = 'admin_modelos/modelo_detail.html'

def modelo_list(request):
    modelo = Modelo.objects.all()
    contexto = {'modelos':modelo}
    return render(request, 'admin_modelos/modelo_list.html', contexto)