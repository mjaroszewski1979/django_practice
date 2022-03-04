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

    context['data'] = Country.objects.annotate(av_pop = Avg('city__population'))

    context['data1'] = Country.objects.filter(Q(name__startswith='un')).annotate(num_cities=Count('city'))

    context['data2'] = Country.objects.filter(Q(name__startswith='un')).aggregate(Min('city__population'))

    context['data3'] = Country.objects.annotate(avg_pop=Avg('city__population')).filter(avg_pop__gt=2000000)

    context['data4'] = Country.objects.annotate(num_cities=Count('city')).aggregate(Min('num_cities'))

    context['data5'] = Country.objects.annotate(num_cities=Count('city', filter=Q(city__population__gt=3000000)))

    context['data6'] = Country.objects.annotate(num_cities=Count('city', filter=Q(city__population__gt=3000000))).order_by('-num_cities')
    

    return render(request, 'cities.html',{'context': context})
