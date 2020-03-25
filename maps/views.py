from django.shortcuts import render
from .models import Person,Place
from services.models import Counter
from django.core import serializers
from django.http import HttpResponse
# from django.contrib.gis import gdal

def default_map(request):
    return render(request, 'maps/default.html', {})

def posts(request):
    posts = Person.objects.all()
    post_list = serializers.serialize('json', posts)

    return HttpResponse(post_list, content_type="text/json-comment-filtered")


def map(request):
    hospital = Place.objects.filter(status=1)
    deaths = Place.objects.filter(status=2)
    corona_case = Place.objects.filter(status=3)
    counter= Counter.objects.first()
    return render(request, 'maps/map.html',
                {'hospital': hospital,
                'deaths': deaths,
                'corona_case': corona_case,
                'counter':counter})
