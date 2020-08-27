"""examensustiLPIII URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from miapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
     path('listar-libro/', views.listar_libro, name="listar_libro"),
    path('eliminar-libro/<int:id>',views.eliminar_libro, name="eliminar_libro"),
    path('listar-autor/', views.listar_autor, name="listar_autor"),
    path('eliminar-autor/<int:id>',views.eliminar_autor, name="eliminar_autor"),
    path('listar-editorial/', views.listar_editorial, name="listar_editorial"),
    path('eliminar-editorial/<int:id>',views.eliminar_editorial, name="eliminar_editorial")
]
