from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, UserDetailsForm
from django.contrib.auth.models import User
from django.contrib import messages
from CAJL.aplications.loginregister.signals import user_created


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
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            # Guarda el formulario sin hacer commit para obtener la instancia del usuario
            user = user_creation_form.save(commit=False)
            user.save()  # Guarda la instancia del usuario ahora

            # Llama a la función de señal con la instancia del usuario
            user_created(sender=user.__class__, instance=user, created=True)
            
            print("Vista de registro ejecutada")
            
            return redirect('home')
    
    return render(request, 'registration/register.html', data)

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


#DATATABLE PARA CARGAR USUARIOS
@login_required
def user_list(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'loginregister/user_list.html', context)

#VISTA PARA DETALLES DE LOS USUARIOS
@login_required
def user_details(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=user)
        if 'editar' in request.POST:
            if form.is_valid():
                form.save()  # Guarda los cambios en la base de datos
                messages.success(request, 'Los datos del usuario han sido actualizados.')
                return redirect('user_list')  # Redirige después de la edición
            else:
                messages.error(request, 'Error al actualizar los datos del usuario.')
        elif 'eliminar' in request.POST:
            user.delete()
            messages.success(request, 'El usuario ha sido eliminado.')
            return redirect('user_list')
    else:
        form = UserDetailsForm(instance=user)
    
    return render(request, 'loginregister/user_details.html', {'form': form, 'user': user})