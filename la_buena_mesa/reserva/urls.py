from django.urls import path
from . import views

urlpatterns = [
    path('reserva/',views.reservas,name='reservar'),
]
