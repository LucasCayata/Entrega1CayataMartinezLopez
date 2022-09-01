from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Productos, Locales, Chefs, Reservas
from AppCoder.forms import ProductosFormulario, LocalesFormulario, ChefsFormulario, ReservasFormulario

# Create your views here.
def inicio(request):
    return render (request, "AppCoder/inicio.html")

def productos(request):
    return render (request, "AppCoder/productos.html")

def locales(request):
    return render (request, "AppCoder/locales.html")

def chefs(request):
    return render (request, "AppCoder/chefs.html")

def reservas(request):
    return render (request, "AppCoder/reservas.html")

def productosFormulario(request):

    if request.method == 'POST':
        miFormulario = ProductosFormulario(request.POST)            
        if miFormulario.is_valid():   
            informacion = miFormulario.cleaned_data
            nombre= informacion.get("nombre")
            codigo = informacion.get("codigo")
            fechaElab= informacion.get("fechaElab")
            fechaVenc= informacion.get("fechaVenc")
            producto = Productos(nombre=nombre, codigo=codigo, fechaElab=fechaElab, fechaVenc=fechaVenc) 
            producto.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Registro producto creado"})
        else: 
            return render(request, "AppCoder/inicio.html", {"mensaje": "Error"})
    else:
        miFormulario= ProductosFormulario() 
        return render(request, "AppCoder/productoFormulario.html", {"formulario":miFormulario})

def localesFormulario(request):

    if request.method == 'POST':
        miFormulario2 = LocalesFormulario(request.POST)            
        if miFormulario2.is_valid():   
            informacion = miFormulario2.cleaned_data
            nombre= informacion.get("nombre")
            direccion = informacion.get("direccion")
            telefono= informacion.get("telefono")
            email= informacion.get("email")
            local = Locales(nombre=nombre, direccion=direccion, telefono=telefono, email=email) 
            local.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Registro producto creado"})
        else: 
            return render(request, "AppCoder/inicio.html", {"mensaje": "Error"})
    else:
        miFormulario2= LocalesFormulario() 
        return render(request, "AppCoder/localFormulario.html", {"formulario":miFormulario2})

def chefsFormulario(request):

    if request.method == 'POST':
        miFormulario3 = ChefsFormulario(request.POST)            
        if miFormulario3.is_valid():   
            informacion = miFormulario3.cleaned_data
            nombre= informacion.get("nombre")
            apellido = informacion.get("apellido")
            especialidad= informacion.get("especialidad")
            chef = Chefs(nombre=nombre, apellido=apellido, especialidad=especialidad) 
            chef.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Registro producto creado"})
        else: 
            return render(request, "AppCoder/inicio.html", {"mensaje": "Error"})
    else:
        miFormulario3= ChefsFormulario() 
        return render(request, "AppCoder/chefFormulario.html", {"formulario":miFormulario3})

def reservasFormulario(request):

    if request.method == 'POST':
        miFormulario4 = ReservasFormulario(request.POST)            
        if miFormulario4.is_valid():   
            informacion = miFormulario4.cleaned_data
            nombre= informacion.get("nombre")
            mesa = informacion.get("mesa")
            comensales= informacion.get("comensales")
            reservado= informacion.get("reservado")
            reserva = Reservas(nombre=nombre, mesa=mesa, comensales=comensales, reservado=reservado) 
            reserva.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Registro producto creado"})
        else: 
            return render(request, "AppCoder/inicio.html", {"mensaje": "Error"})
    else:
        miFormulario4= ReservasFormulario() 
        return render(request, "AppCoder/reservaFormulario.html", {"formulario":miFormulario4})
        
                
def busquedaCodigo(request):
    return render(request, "AppCoder/busquedaCodigo.html")      

def buscar(request):
    if request.GET["codigo"]:
        codigo=request.GET["codigo"]
        productos=Productos.objects.filter(codigo=codigo)
        if len(productos)!=0:
            return render(request, "AppCoder/resultadoBusqueda.html", {"productos":productos}) 
        else:
            return render(request, "AppCoder/resultadoBusqueda.html", {"mensaje": "No hay productos"})      
    else:
        return render(request, "AppCoder/busquedaCodigo.html", {"mensaje": "No enviaste datos"})



def busquedaDireccion(request):
    return render(request, "AppCoder/busquedaDireccion.html")      

def buscarDireccion(request):
    if request.GET["direccion"]:
        direccion=request.GET["direccion"]
        locales=Locales.objects.filter(direccion=direccion)
        if len(locales)!=0:
            return render(request, "AppCoder/resultadoBusquedaDir.html", {"locales":locales}) 
        else:
            return render(request, "AppCoder/resultadoBusquedaDir.html", {"mensaje": "No hay locales"})      
    else:
        return render(request, "AppCoder/busquedaDireccion.html", {"mensaje": "No enviaste datos"})