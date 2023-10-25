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
from .views import prices_list, carga_datos, detalles_precio
urlpatterns = [
    path('prices_list/', prices_list, name='prices_list'),
    path('prices_add/', carga_datos, name='prices_add'),
    path('detalles_precio/<int:price_id>/', detalles_precio, name='detalles_precio'),
]