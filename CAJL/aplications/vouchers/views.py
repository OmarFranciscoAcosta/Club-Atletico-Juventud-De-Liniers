from django.shortcuts import render,redirect, get_object_or_404
from .models import vouchers
from .forms import VouchersForm
from django.contrib import messages
# Create your views here.

#VISTA PARA GENERAR UNA DATATABLE.
def comprobantes_list(request):
    comprobantes = vouchers.objects.all()
    return render(request, 'vouchers/vouchers_list.html', {'comprobantes': comprobantes})



#VISTA PARA GENERAR LA CARGA DE UN COMPROBANTE NUEVO.
def carga_comprobante(request):
    if request.method == 'POST':
        # Si se envió un formulario (POST), procesa los datos y guárdalos en la base de datos.
        form = VouchersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comprobantes')  # Redirige a la página de lista de socios (ajusta la URL según tu configuración)
    else:
        # Si no se envió un formulario (GET), muestra el formulario para agregar un socio.
        form = VouchersForm()
    
    return render(request, 'vouchers/carga_comprobante.html', {'form': form})

#VISTA PARA GENERAR LOS DETALLES DEL COMPROBANTE
def detalles_comprobante (request, vouchers_id):
    voucher = get_object_or_404(vouchers, id=vouchers_id)
    
    if request.method == 'POST':
        if 'editar' in request.POST:
            form = VouchersForm(request.POST, instance=voucher)
            if form.is_valid():
                form.save()
                messages.success(request, 'Los datos del comprobante han sido actualizados.')
                return redirect('comprobantes')  # Reemplaza 'prices-list' con la URL de la lista de precios
            else:
                messages.error(request, 'Error al actualizar los datos del comprobante.')
        elif 'eliminar' in request.POST:
            voucher.delete()
            messages.success(request, 'El comprobante ha sido eliminado.')
            return redirect('comprobantes')  # Reemplaza 'prices-list' con la URL de la lista de precios
    else:
        form = VouchersForm(instance=voucher)
    
    return render(request, 'vouchers/detalles_comprobante.html', {'form': form, 'voucher': voucher})