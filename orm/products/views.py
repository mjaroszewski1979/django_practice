from django.shortcuts import render
from .models import Customer, Product, Order, LineItem
from django.db import connection
from django.db.models import Q, Min, Avg, Count, Sum, F, Value
from django.db.models.functions import Concat
from datetime import timedelta





def home(request):
    context = {}
    '''context['sub_total'] = LineItem.objects.select_related('order', 'product').all().annotate(sub_total=F('product__price') * F('quantity'))
    context['total'] = LineItem.objects.aggregate(total=Sum(F('product__price') * F('quantity')))
    context['average'] = LineItem.objects.aggregate(average=Avg(F('product__price') * F('quantity')))
    context['dates_match'] = Order.objects.filter(order_date=F('delivered_date')).order_by('order_date')
    context['del_time'] = Order.objects.select_related('customer').all().annotate(del_time=F('delivered_date') - F('order_date')).filter(del_time__lte=timedelta(days=2)).filter(Q(customer__email__startswith='j') & Q(customer__last_name__endswith='ski'))
    context['concat'] = Customer.objects.annotate(full_name=Concat('first_name', Value(" "), 'last_name')).filter(full_name__icontains='ja')
    # For models with foreign key
    context['orders'] = Order.objects.select_related('customer').all().filter(Q(customer__city__startswith='l'))'''
    # For models with many to many relationship
    context['products'] = Order.objects.prefetch_related('products').all().filter(products__price__gt=500)

 

    return render(request, 'home.html',{'context': context})



