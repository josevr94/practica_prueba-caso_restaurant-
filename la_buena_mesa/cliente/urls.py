from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('registro_cliente',views.registro_cliente,name='registro_cliente'),
]
