from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from .models import payments
from .forms import PaymentsForm 
from django.contrib import messages

# Create your views here.


#RENDER DATOS PARA DATATABLE
def payments_list(request):
    # Recupera los pagos desde la base de datos
    payments_data = payments.objects.all()

    # Pasa los datos a la plantilla
    context = {'payments_data': payments_data}
    return render(request, 'payments/payments_list.html', context)

#RENDER DATOS PARA CARGAR COMPROBANTE
def carga_comprobante(request):
    if request.method == 'POST':
        form = PaymentsForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos

            # Devuelve una respuesta JSON para indicar éxito
            return JsonResponse({'success': True})

    # Resto del código como lo tenías originalmente
    else:
        form = PaymentsForm()

    return render(request, 'payments/carga_comprobante.html', {'form': form})

#RENDER PARA DETALLES DEL COMPROBANTE
def detalles_cpb(request, payments_id):
    payment = get_object_or_404(payments, id=payments_id)
    
    if request.method == 'POST':
        if 'editar' in request.POST:
            form = PaymentsForm(request.POST, instance=payment)
            if form.is_valid():
                form.save()
                messages.success(request, 'Los datos del comprobante han sido actualizados.')
                return redirect('payments_list')
            else:
                messages.error(request, 'Error al actualizar los datos del comprobante.')
        elif 'eliminar' in request.POST:
            payments.delete()
            messages.success(request, 'El comprobante ha sido eliminado.')
            return redirect('payments_list')
    else:
        form = PaymentsForm(instance=payment)
    
    return render(request, 'payments/detalles_comprobante.html', {'form': form, 'payment': payment})


