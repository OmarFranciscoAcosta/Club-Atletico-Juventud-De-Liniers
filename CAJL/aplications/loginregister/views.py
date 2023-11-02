from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home (request):
    return render (request, 'loginregister/home.html')

#AUTENTICACION EN LA PESTAÑA PARTNERS
@login_required
def partners (request):
    return render (request, 'loginregister/partners.html')


#LOGOUT
def exit (request):
    logout(request)
    return redirect ('home')

#REGISTRO
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }    
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm (data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            
            return redirect('home')
    
    return render (request, 'registration/register.html',data)

#RECUPERAR CONTRASEÑA
def custom_password_reset(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Actualiza la sesión del usuario y vuelve a autenticarlo
            update_session_auth_hash(request, user)
            return redirect('password_reset_complete')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'custom_password_reset_form.html', {'form': form})