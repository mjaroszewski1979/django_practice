from django.shortcuts import render,  get_object_or_404
from .models import Country,City
from django.db import connection
from django.db.models import Q, Min, Avg, Count





def cities_list(request):
    context = {}
    cities = City.objects.all()
    context['vars'] = vars(cities[0])
    # Minimal population for each city
    min_population = City.objects.annotate(Min('population'))
    context['min_population'] = vars(min_population[1])
    # Average population for all cities
    avg_population = City.objects.aggregate(Avg('population'))
    context['avg_population'] = avg_population
    # Number of cities per Country
    city_num = Country.objects.annotate(result = Count('city'))
    context['city_num'] = city_num[0].result
    # Cities with population above average
    above_avg = City.objects.filter(Q(population__gt=avg_population['population__avg']))
    context['above_avg'] = above_avg
    all_countries = Country.objects.all()
    # Average population for cities in country number 3
    context['avg_all_cities'] = City.objects.filter(Q(country__name=all_countries[3])).aggregate(Avg('population'))
    # Average population in cities for particular country
    context['data'] = Country.objects.annotate(av_pop = Avg('city__population'))
    # Number of cities for countries which names starting with un
    context['data1'] = Country.objects.filter(Q(name__startswith='un')).annotate(num_cities=Count('city'))
    # Minimal population in cities located in countries with names starting with un
    context['data2'] = Country.objects.filter(Q(name__startswith='un')).aggregate(Min('city__population'))
    # Average population in cities with population greater than 2 mln
    context['data3'] = Country.objects.annotate(avg_pop=Avg('city__population')).filter(avg_pop__gt=2000000)
    # Minimal number of cities for particular country
    context['data4'] = Country.objects.annotate(num_cities=Count('city')).aggregate(Min('num_cities'))
    # Number of cities for partcicular country with population greater than 3 mln
    context['data5'] = Country.objects.annotate(num_cities=Count('city', filter=Q(city__population__gt=3000000)))
    # Number of cities for partcicular country with population greater than 3 mln in ascending order
    context['data6'] = Country.objects.annotate(num_cities=Count('city', filter=Q(city__population__gt=3000000))).order_by('-num_cities')
    

    return render(request, 'cities.html',{'context': context})

def detail(request, slug=None): 
    city = get_object_or_404(City, slug=slug)
    return render(request, 'detail.html', {'city': city})

