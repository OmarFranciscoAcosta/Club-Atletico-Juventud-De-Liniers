from django.shortcuts import render
from .models import payments

# Create your views here.


#RENDER DATOS PARA DATATABLE
def payments_list(request):
    # Recupera los pagos desde la base de datos
    payments_data = payments.objects.all()

    # Pasa los datos a la plantilla
    context = {'payments_data': payments_data}
    return render(request, 'payments/payments_list.html', context)