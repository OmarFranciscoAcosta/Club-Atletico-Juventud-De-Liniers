from django.shortcuts import render
from .models import vouchers
# Create your views here.

#VISTA PARA GENERAR UNA DATATABLE.
def comprobantes_list(request):
    comprobantes = vouchers.objects.all()
    return render(request, 'vouchers/comprobantes.html', {'comprobantes': comprobantes})