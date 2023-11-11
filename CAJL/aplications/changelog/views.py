from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChangeLog
# Create your views here.

#Datatable con datos del changelog
@login_required
def change_log_view(request):
    change_logs = ChangeLog.objects.all()
    return render(request, 'changelog/change_log.html', {'change_logs': change_logs})