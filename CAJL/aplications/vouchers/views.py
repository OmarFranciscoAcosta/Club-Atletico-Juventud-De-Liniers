from django.shortcuts import render,redirect
from .models import vouchers
from .forms import VouchersForm

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