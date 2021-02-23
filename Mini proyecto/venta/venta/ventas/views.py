from django.shortcuts import render
from django.http import HttpResponse
from .models import Clientes

# Create your views here.

def homepage(request):
    return render(request, "ventas/inicio.html",{"clientes":Clientes.objects.all})
    

