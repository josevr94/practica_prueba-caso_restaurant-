from django.shortcuts import render,redirect
from .forms import ClienteForm


def home(request):
    return render(request,'cliente/menu.html')
# Create your views here.

def registro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request,'cliente/registro_cliente.html',{'form':form})
        