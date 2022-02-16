from django.urls import path,include
from . import views
from .views import ProductoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns =[
    path('buscar/', views.Buscar_view,name='Buscar_view'),
    path('<slug:categoria_slug>/<slug:producto_slug>', views.Producto_view,name='Producto_view'),
    path('<slug:categoria_slug>/', views.Categoria_view,name='Categoria_view'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
