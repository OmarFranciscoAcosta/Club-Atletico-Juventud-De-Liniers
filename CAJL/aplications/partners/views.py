from django.shortcuts import render, redirect, get_object_or_404
from .models import partners
from .forms import PartnerForm
from django.contrib import messages
# Create your views here.

#Datatable con modelo Partners
def datatable_view(request):
    partners_data = partners.objects.select_related('localidad')
    data = []

    for partner in partners_data:
        data.append({
            'id': partner.id,
            'nombre_completo': partner.nombre_completo,
            'dni': partner.dni,
            'fecha_nacimiento': partner.fecha_nacimiento,
            'direccion': partner.direccion,
            'distrito': partner.get_distrito_display(),  # Usamos get_<field_name>_display() para campos choices
            'localidad': partner.localidad.municipio_nombre,
            'telefono1': partner.telefono1,
            'telefono2': partner.telefono2,
            'correo': partner.correo,
            'descripcion': partner.descripcion,
            'apto_fisico': partner.apto_fisico,
            'fecha_vencimiento_apto_fisico': partner.fecha_vencimiento_apto_fisico,
            'fecha_vencimiento_fichaje': partner.fecha_vencimiento_fichaje,
            'compite': partner.compite,
            'socio_activo': partner.socio_activo,
        })

    return render(request, 'partners/partners_list.html', {'data': data})

#Agregar Socio
def agregar_socio(request):
    if request.method == 'POST':
        # Si se envió un formulario (POST), procesa los datos y guárdalos en la base de datos.
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('socios')  # Redirige a la página de lista de socios (ajusta la URL según tu configuración)
    else:
        # Si no se envió un formulario (GET), muestra el formulario para agregar un socio.
        form = PartnerForm()
    
    return render(request, 'partners/agregar_socio.html', {'form': form})


#Detalles del socio con actualizar y eliminar, dejando mensajes de avisos
def detalles(request, partner_id):
    partner = get_object_or_404(partners, id=partner_id)
    
    if request.method == 'POST':
        if 'editar' in request.POST:
            form = PartnerForm(request.POST, instance=partner)
            if form.is_valid():
                form.save()
                messages.success(request, 'Los datos del socio han sido actualizados.')
                return redirect('socios')
        elif 'eliminar' in request.POST:
            partner.delete()
            messages.success(request, 'El socio ha sido eliminado.')
            return redirect('socios')  # Redirige a donde desees después de la eliminación
    else:
        form = PartnerForm(instance=partner)
    
    return render(request, 'partners/detalles_socio.html', {'form': form, 'partner': partner})