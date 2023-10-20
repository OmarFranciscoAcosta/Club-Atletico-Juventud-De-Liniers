from django.shortcuts import render
from .models import activities


# Create your views here.
def activities_list(request):
    activities_data = activities.objects.all()
    return render(request, 'activities/activities_list.html', {'activities_data': activities_data})