from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.db.models import Q, Min, Avg, Count
from .models import Country,City
from .forms import CityFormSet, CityModelForm





def cities_list(request):
    context = {}
    '''cities = City.objects.all()
    # List of values for given field, flat=True to get python list
    context['val_list'] = City.objects.values_list('country__name', flat=True).get(pk=3)
    # Filter using regular expression
    cities_ag = City.objects.filter(name__iregex=r"^[a-g].*$")
    germany = City.objects.filter(country__name='germany')
    context['iregex'] = cities_ag
    # Count number of objects
    context['iregex_count'] = City.objects.filter(name__iregex=r"^[a-g].*$").count()
    # Intersection
    inter = cities_ag & germany
    context['inter'] = inter[0].name
    context['inter1'] = City.objects.filter(name__iregex=r"^[a-g].*$", country__name='germany')[0].name
    # Difference between sets
    context['diff'] = cities_ag.exclude(country__name='germany')
    context['only'] = City.objects.filter(Q(population__gt=3000000)).only('slug')'''
    items = City.objects.filter(Q(name__icontains='a'))
    country_ids = items.values_list('country__id', flat=True).distinct()
    context['bulk'] = Country.objects.in_bulk(country_ids)
    '''context['vars'] = vars(cities[0])
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
    context['data6'] = Country.objects.annotate(num_cities=Count('city', filter=Q(city__population__gt=3000000))).order_by('-num_cities')'''
    

    return render(request, 'cities.html',{'context': context})

def detail(request, slug=None): 
    city = get_object_or_404(City, slug=slug)
    return render(request, 'detail.html', {'city': city})

'''def create_city(request, pk):
    country = Country.objects.get(pk=pk)
    formset = CityFormSet(request.POST or None)

    if request.method == 'POST':
        if formset.is_valid():
            formset.instance = country
            formset.save()
            return redirect('cities:create-city', pk=country.id)

    context = {
        'formset' : formset,
        'country' : country
    }

    return render(request, 'create_city.html', context)'''
    
def create_city(request, pk):
    country = Country.objects.get(pk=pk)
    cities = City.objects.filter(country=country)
    form = CityModelForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            city = form.save(commit=False)
            city.country = country
            city.save()
            return redirect('cities:detail-city', pk=city.id)
        else:
            return render(request, 'partials/city_form.html', {'form':form})

    context = {
        'form' : form,
        'country' : country,
        'cities' : cities
    }

    return render(request, 'create_city.html', context)

def create_city_form(request):
    context = {
        'form' : CityModelForm()
    }
    return render(request, 'partials/city_form.html', context)

def update_city(request, pk):
    city = City.objects.get(pk=pk)
    form = CityModelForm(request.POST or None, instance=city)

    if request.method == 'POST':
        if form.is_valid():
            city = form.save()
            return redirect('cities:detail-city', pk=city.id)

    context = {
        'form' : form, 
        'city' : city
    }
    return render(request, 'partials/city_form.html', context)

def detail_city(request, pk):
    city = City.objects.get(pk=pk)
    context = {
        'city' : city
    }
    return render(request, 'city_detail.html', {'city': city})

def delete_city(request, pk):
    city = City.objects.get(pk=pk)
    city.delete()
    return HttpResponse('')



