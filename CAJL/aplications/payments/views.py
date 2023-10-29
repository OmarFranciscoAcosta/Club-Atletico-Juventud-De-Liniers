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
        # Si se envió un formulario (POST), procesa los datos y guárdalos en la base de datos.
        form = PaymentsForm(request.POST)
        if form.is_valid():
            comprobante = form.save(commit=False)  # Guarda la instancia sin hacer commit
            comprobante.user = request.user  # Asigna el usuario actual
            comprobante.save()  # Ahora puedes guardar la instancia con el usuario asignado
            return redirect('payments_list')  # Redirige a la página de lista de socios (ajusta la URL según tu configuración)
        
    else:
        # Si no se envió un formulario (GET), muestra el formulario para agregar un socio.
        form = PaymentsForm()
    
    return render(request, 'payments/carga_comprobante.html', {'form': form})







#RENDER PARA DETALLES DEL COMPROBANTE
def detalles_comprobante(request, payments_id):
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
            payment.delete()
            messages.success(request, 'El comprobante ha sido eliminado.')
            return redirect('payments_list')
    else:
        form = PaymentsForm(instance=payment)
    
    return render(request, 'payments/detalles_comprobante.html', {'form': form, 'payment': payment})
