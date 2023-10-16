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
from CAJL.aplications import loginregister
from .views import custom_password_reset, home, partners, exit, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name='home'),
    path('partners/', partners, name='partners'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('reset_password/', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
