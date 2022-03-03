from django.shortcuts import render
from .models import Country,City
from django.db import connection
from django.db.models import Q, Min, Avg, Count





def cities_list(request):
    context = {}
    cities = City.objects.all()
    context['vars'] = vars(cities[0])
    min_population = City.objects.annotate(Min('population'))
    context['min_population'] = vars(min_population[1])
    avg_population = City.objects.aggregate(Avg('population'))
    context['avg_population'] = avg_population
    city_num = Country.objects.annotate(result = Count('city'))
    context['city_num'] = city_num[0].result
    above_avg = City.objects.filter(Q(population__gt=avg_population['population__avg']))
    context['above_avg'] = above_avg
    all_countries = Country.objects.all()

    context['avg_all_cities'] = City.objects.filter(Q(country__name=all_countries[3])).aggregate(Avg('population'))
    context['data'] = all_countries[4]
    

    return render(request, 'cities.html',{'context': context})
