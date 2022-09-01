from django.urls import path
from .views import *


urlpatterns = [
    path("", inicio, name='inicio'),
    path("productos/", productos, name='productos'),
    path("locales/", locales, name='locales'),
    path("chefs/", chefs, name='chefs'),
    path("reservas/", reservas, name='reservas'),
    path("productoFormulario/", productosFormulario, name='productoFormulario'),
    path("localFormulario/", localesFormulario, name='localFormulario'),
    path("chefFormulario/", chefsFormulario, name='chefFormulario'),
    path("reservaFormulario/", reservasFormulario, name='reservaFormulario'),
    path("busquedaCodigo/", busquedaCodigo, name='busquedaCodigo'),
    path("buscar/", buscar, name='buscar'),
    path("busquedaDireccion/", busquedaDireccion, name='busquedaDireccion'),
    path("buscarDireccion/", buscarDireccion, name='buscarDireccion'),

]