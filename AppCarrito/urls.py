from django.urls import path

from . import views


urlpatterns =[
    path('', views.CarritoDetalles_view,name='CarritoDetalles_view'),
    path('exitoso', views.Correcto_view,name='Correcto_view'),
]