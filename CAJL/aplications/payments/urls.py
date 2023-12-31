"""
URL configuration for CAJL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views


urlpatterns = [
    path('pagos/', views.payments_list, name='payments_list'),
    path('agregar_comprobante/', views.carga_comprobante, name='agregar_comprobante'),
    path('detalles_comprobante/<int:payments_id>/', views.detalles_comprobante, name='detalles_comprobante'),
    path('imprimir_comprobante/<int:payments_id>/', views.imprimir_comprobante, name='imprimir_comprobante'),
    # Agrega más rutas si es necesario
]