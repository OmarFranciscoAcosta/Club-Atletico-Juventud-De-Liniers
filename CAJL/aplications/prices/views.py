from django.shortcuts import render
from django.http import JsonResponse
from .models import prices
# Create your views here.

#Vista para generar la datatable de precios de las actividades:
def prices_list(request):
    price_data = prices.objects.all()

    context = {
        'price_data': price_data,
    }

    return render(request, 'prices/prices_list.html', context)

