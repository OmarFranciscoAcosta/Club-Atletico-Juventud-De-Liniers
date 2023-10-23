from django.shortcuts import render
from django.http import JsonResponse
from .forms import PricesForm
from .models import prices
# Create your views here.

#Vista para generar la datatable de precios de las actividades:
def prices_list(request):
    price_data = prices.objects.all()

    context = {
        'price_data': price_data,
    }

    return render(request, 'prices/prices_list.html', context)

#Vista para generar la carga de un precio de la actividad:
def carga_datos(request):
    if request.method == 'POST':
        form = PricesForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos

            # Devuelve una respuesta JSON para indicar éxito
            return JsonResponse({'success': True})

    # Resto del código como lo tenías originalmente
    else:
        form = PricesForm()

    return render(request, 'prices/carga_precio.html', {'form': form})