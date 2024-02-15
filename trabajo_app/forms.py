from django import forms

class Electrodomestico_formulario(forms.Form):
    nombre = forms.CharField()
    modelo = forms.CharField()

class Cliente_form(forms.Form):
    cliente = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)

class Empleado_form(forms.Form):
    empleado = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)

class Buscar(forms.Form):
    modelo = forms.CharField(max_length=30)


