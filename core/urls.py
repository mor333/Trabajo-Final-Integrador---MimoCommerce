"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('security/', include('apps.security.urls', namespace='security')),
    path('', include('apps.inicio.urls', namespace='inicio')),
    path('usuario/', include('apps.usuario.urls', namespace='usuario')),
    path('admin/', admin.site.urls),
    path('stock/', include('apps.stock.urls', namespace='stock')),
    path('empresa/', include('apps.empresa.urls', namespace='empresa')),
    path('productos/', include('apps.productos.urls', namespace='productos')),
    path('servicios/', include('apps.servicios.urls', namespace='servicios')),
    path('turnos/', include('apps.turnos.urls', namespace='turnos')),
]
