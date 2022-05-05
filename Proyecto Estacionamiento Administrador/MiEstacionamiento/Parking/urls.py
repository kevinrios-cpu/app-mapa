from django.urls import path
from .views import PlaceView,inicio


urlpatterns = [
    path('home',PlaceView.as_view(),name='home'),
    path('',inicio,name='inicio'),
]