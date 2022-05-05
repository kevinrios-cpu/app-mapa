from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView
from .models import Direccion, Vehiculo,Usuario
from django.urls import reverse_lazy


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
    #Objetos del modelo
    placeObjects=model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[token] = key
        context[parkings] = Direccion.objects.all()
        return context

def inicio(request):
    return render(request, 'inicio.html', context={token:key, parkings:PlaceView.placeObjects},)

