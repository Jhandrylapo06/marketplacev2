from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import routers
from .import views
from .views import UsuarioViewSet

router = routers.DefaultRouter()
router.register(r'users', UsuarioViewSet)

urlpatterns =[
    path('usuario/', views.Usuario_view,name='usuario'),
    path('usuarioadmin/', views.UsuarioAdmin_view,name='usuarioadmin'),
    path('añadirproducto/', views.AñadirProducto_view,name='añadirproducto'),
    path('editarusuario/', views.EditarUsuario_view,name='EditarUsuario_view_view'),
    path('editarproducto/<int:pk>/', views.EditarProducto_view,name='EditarProducto_view'),

    path('salir/', auth_views.LogoutView.as_view(),name='salir'),
    path('ingresar/', auth_views.LoginView.as_view(template_name='user/login.html'),name='ingresar'),
    path('', views.vendors,name='vendors'),
    path('<int:vendor_id>/', views.vendor,name='vendor'),

]
urlpatterns += [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]