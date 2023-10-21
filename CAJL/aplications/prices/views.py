from django.shortcuts import render
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.http import JsonResponse
from .models import prices
# Create your views here.

#Vista para generar la datatable de precios de las actividades:
class PricesListJson(BaseDatatableView):
    model = prices
    columns = ['anio', 'mes', 'actividad__nombre_actividad', 'valor_clase_consulta', 'valor_mensual_fijo', 'valor_mensual_1semana', 'valor_mensual_2semana', 'valor_clase_3semana', 'valor_fichaje_anual', 'valor_libre', 'cuota_social', 'mes_impago']

    def render_column(self, row, column):
        if column == 'actividad__nombre_actividad':
            return row.actividad.nombre_actividad
        return super(PricesListJson, self).render_column(row, column)

    def get_initial_queryset(self):
        return prices.objects.all()
    def prepare_results(self, qs):
        data = []
        for item in qs:
            data.append([
                item.anio,
                item.get_mes_display(),
                item.actividad.nombre_actividad,
                item.valor_clase_consulta,
                item.valor_mensual_fijo,
                item.valor_mensual_1semana,
                item.valor_mensual_2semana,
                item.valor_clase_3semana,
                item.valor_fichaje_anual,
                item.valor_libre,
                item.cuota_social,
                item.mes_impago
            ])
        return data
def prices_list(request):
    return render(request, 'prices/prices_list.html')
