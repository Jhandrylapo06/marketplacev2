
from django.urls import path

from .import views

urlpatterns =[
    path('', views.Principal_view,name='principal'),
    path('contacto/', views.Contacto_view,name='contacto'),

]