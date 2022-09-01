from django import forms

class ProductosFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    codigo = forms.IntegerField()
    fechaElab= forms.DateField()
    fechaVenc= forms.DateField()

class LocalesFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    direccion= forms.CharField(max_length=30)
    telefono= forms.IntegerField()
    email= forms.EmailField()

class ChefsFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    especialidad= forms.CharField(max_length=30)

class ReservasFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    mesa= forms.IntegerField()  
    comensales= forms.IntegerField()
    reservado = forms.BooleanField()

    

