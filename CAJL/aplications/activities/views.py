from django.shortcuts import render, redirect, get_object_or_404
from .forms import ActivitiesForm
from .models import activities
from django.contrib import messages


# Create your views here.
#Vista datatable actividades
def activities_list(request):
    activities_data = activities.objects.all()
    
    tipos_actividad = activities_data.values_list('tipo_actividad', flat=True).distinct()
    
    context = {
        'activities_data': activities_data,
        'tipos_actividad': tipos_actividad,
    }
    
    #return render(request, 'activities/activities_list.html', {'activities_data': activities_data})
    return render(request, 'activities/activities_list.html', context)

#Vista modificar datos, trayendo los mismos
def detallesact(request, activities_id):
    activity = get_object_or_404(activities, id=activities_id)
    
    if request.method == 'POST':
        if 'editar' in request.POST:
            form = ActivitiesForm(request.POST, instance=activity)
            if form.is_valid():
                form.save()
                messages.success(request, 'Los datos de la actividad han sido actualizados.')
                return redirect('actividades')
            else:
                messages.error(request, 'Error al actualizar los datos de la actividad.')
        elif 'eliminar' in request.POST:
            activity.delete()
            messages.success(request, 'La actividad ha sido eliminada.')
            return redirect('actividades')
    else:
        form = ActivitiesForm(instance=activity)
    
    return render(request, 'activities/detalles_actividades.html', {'form': form, 'activity': activity})

#Vista Agregar una nueva actividad
def agregar_actividad(request):
    if request.method == 'POST':
        # Si se envió un formulario (POST), procesa los datos y guárdalos en la base de datos.
        form = ActivitiesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actividades')  # Redirige a la página de lista de socios (ajusta la URL según tu configuración)
    else:
        # Si no se envió un formulario (GET), muestra el formulario para agregar un socio.
        form = ActivitiesForm()
    
    return render(request, 'activities/agregar_actividad.html', {'form': form})