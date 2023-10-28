from django.shortcuts import render
from .models import ChangeLog
# Create your views here.
def change_log_view(request):
    change_logs = ChangeLog.objects.all()
    return render(request, 'changelog/change_log.html', {'change_logs': change_logs})