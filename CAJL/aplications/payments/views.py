from django.shortcuts import render
from django.http import JsonResponse
from .models import payments
from .forms import PaymentsForm 

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