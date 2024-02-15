from django.shortcuts import render
from django.http import HttpResponse
from .models import electrodomestico, Cliente, Empleado
# Create your views here.
from trabajo_app.forms import Electrodomestico_formulario, Cliente_form, Empleado_form, Buscar
 
def electrodomes_form(request):
    
    
 
    if request.method == "POST":          
 
            miFormulario = Electrodomestico_formulario(request.POST)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  cliente = electrodomestico(nombre=informacion["nombre"], modelo=informacion["modelo"])
                  cliente.save()
                  return render(request, "proyecto_app/index.html")
    else:
            miFormulario = Electrodomestico_formulario()
 
    return render(request, "proyecto_app/compraformulario.html", {"miFormulario": miFormulario})

def inicio(request):
    return render(request, "proyecto_app/index.html")

def Clientes(request):
     
      if request.method == "POST":
 
            miFormulario = Cliente_form(request.POST)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  cliente = Cliente(cliente=informacion["cliente"], email=informacion["email"])
                  cliente.save()
                  return render(request, "proyecto_app/index.html")
      else:
            miFormulario = Cliente_form()
 
      return render(request, "proyecto_app/cliente.html", {"miFormulario": miFormulario})

def Empleados(request):
     
      if request.method == "POST":
 
            miFormulario = Empleado_form(request.POST)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  cliente = Empleado(empleado=informacion["empleado"], apellido=informacion["apellido"], email=informacion["email"])
                  cliente.save()
                  return render(request, "proyecto_app/index.html")
      else:
            miFormulario = Empleado_form()
 
      return render(request, "proyecto_app/empleados.html", {"miFormulario": miFormulario})

def buscar_c(request):
      if request.method == "POST":
            miFormulario= Buscar(request.POST)
            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  compra = electrodomestico.objects.filter(modelo__icontains=info["modelo"])
                  return render(request, "proyecto_app/busqueda.html", {
                        "miFormulario": miFormulario,
                        "compra": compra})

      else:
            miFormulario = Buscar()
      
      return render(request, "proyecto_app/busqueda.html", {"miFormulario": miFormulario})