from django.shortcuts import render
from .models import Location

def map_view(request):
    locations = Location.objects.all()
    return render(request, 'test_app/map.html', {'locations': locations})

