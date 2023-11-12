from django.shortcuts import render, redirect, get_object_or_404
from .forms import PricesForm
from .models import prices
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

#Vista para generar la datatable de precios de las actividades:
@login_required
def prices_list(request):
    price_data = prices.objects.all()

    context = {
        'price_data': price_data,
    }

    return render(request, 'prices/prices_list.html', context)

#Vista para generar la carga de un precio de la actividad:
@login_required
def carga_datos(request):
    if request.method == 'POST':
        # Si se envió un formulario (POST), procesa los datos y guárdalos en la base de datos.
        form = PricesForm(request.POST)
        if form.is_valid():
            price = form.save(commit=False)
            price.user = request.user
            price.save()
            return redirect('prices_list')  # Redirige a la página de lista de socios (ajusta la URL según tu configuración)
        
    else:
        # Si no se envió un formulario (GET), muestra el formulario para agregar un socio.
        form = PricesForm()
    
    return render(request, 'prices/carga_precio.html', {'form': form})


#Vista para generar los detalles de esa carga del precio de la actividad:
@login_required
def detalles_precio(request, price_id):
    price = get_object_or_404(prices, id=price_id)
    
    if request.method == 'POST':
        if 'editar' in request.POST:
            form = PricesForm(request.POST, instance=price)
            if form.is_valid():
                updated_price = form.save(commit=False)
                updated_price.user = request.user
                updated_price.save()
                messages.success(request, 'Los datos del precio han sido actualizados.')
                return redirect('prices_list')
            else:
                messages.error(request, 'Error al actualizar los datos del precio.')
        elif 'eliminar' in request.POST:
            
            deleted_price = price
            deleted_price.user = request.user
            
            price.delete()
            messages.success(request, 'Los precios de la actividad ha sido eliminados.')
            return redirect('prices_list')
    else:
        form = PricesForm(instance=price)
    
    return render(request, 'prices/detalles_precio.html', {'form': form, 'price': price})
    
    
    
    
