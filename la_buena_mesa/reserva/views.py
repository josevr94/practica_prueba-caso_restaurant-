from django.shortcuts import render,redirect
from .models import Reserva
from .forms import ReservaForm
# Create your views here.

def reservas(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')  # Redirigir a una página de éxito
        
    else:
        form = ReservaForm()
        return render(request, 'reserva/crear_reserva.html', {'form': form})