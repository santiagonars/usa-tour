from django.shortcuts import render, get_object_or_404
from .models import Place

# Create your views here.
def home(request):
    places = Place.objects
    return render(request, 'places/home.html', {'places':places})

def detail(request, place_id):
    place_detail = get_object_or_404(Place, pk=place_id)
    return render(request, 'places/detail.html', {'place':place_detail})