from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import PricesForm
from .models import prices
from django.contrib import messages
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

#Vista para generar los detalles de esa carga del precio de la actividad:
def detalles_precio(request, price_id):
    price = get_object_or_404(prices, id=price_id)
    
    if request.method == 'POST':
        if 'editar' in request.POST:
            form = PricesForm(request.POST, instance=price)
            if form.is_valid():
                form.save()
                messages.success(request, 'Los datos del precio han sido actualizados.')
                return redirect('prices_list')
            else:
                messages.error(request, 'Error al actualizar los datos del precio.')
        elif 'eliminar' in request.POST:
            price.delete()
            messages.success(request, 'Los precios de la actividad ha sido eliminados.')
            return redirect('prices_list')
    else:
        form = PricesForm(instance=price)
    
    return render(request, 'prices/detalles_precio.html', {'form': form, 'price': price})
    
    
    
    
