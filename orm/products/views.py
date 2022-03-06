from django.shortcuts import render
from .models import Customer, Product, Order, LineItem
from django.db import connection
from django.db.models import Q, Min, Avg, Count, Sum, F
from datetime import timedelta





def home(request):
    context = {}
    context['sub_total'] = LineItem.objects.annotate(sub_total=F('product__price') * F('quantity'))
    context['total'] = LineItem.objects.aggregate(total=Sum(F('product__price') * F('quantity')))
    context['average'] = LineItem.objects.aggregate(average=Avg(F('product__price') * F('quantity')))
    context['dates_match'] = Order.objects.filter(order_date=F('delivered_date')).order_by('order_date')
    context['del_time'] = Order.objects.annotate(del_time=F('delivered_date') - F('order_date')).filter(del_time__lte=timedelta(days=2)).filter(Q(customer__email__startswith='j') & Q(customer__last_name__endswith='ski'))

    

    return render(request, 'home.html',{'context': context})
