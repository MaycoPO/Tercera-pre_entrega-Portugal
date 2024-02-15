from django.urls import path
from trabajo_app import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Clientes/', views.Clientes, name="Clientes"),
    path('electrodomes-form/', views.electrodomes_form, name="electrodomesticos-form"),
    path('Empleados/', views.Empleados, name="Empleados"),
    path("Busquedas-comp/", views.buscar_c, name="busquedas"),
]


