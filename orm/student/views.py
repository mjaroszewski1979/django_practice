from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q


'''def student_list(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'index.html',{'posts':posts})

def student_list(request):
    posts = Student.objects.filter(surname__startswith='jaroszewski') | Student.objects.filter(surname__startswith='kowalski') | Student.objects.filter(surname__endswith='ski')

    print(posts)
    print(connection.queries)

    return render(request, 'index.html',{'posts':posts})'''

def student_list(request):
    context = {}
    all_studs = Student.objects.all()
    context['all'] = all_studs
    context['data'] = Student.objects.filter(Q(surname__endswith='ski') & ~Q (surname__startswith='jaro'))
    context['data1'] = Student.objects.filter(surname__startswith='jaroszewski') | Student.objects.filter(surname__startswith='kowalski')
    context['data2'] = Student.objects.all()
    context['data3'] = Student.objects.filter(Q(age__gt=30) & Q(age__lt=40))
    context['data4'] = all_studs.exclude(Q(firstname__endswith='ej') & ~Q (classroom=2))

    print(context['data'].query)
    print(connection.queries)

    return render(request, 'index.html',{'context': context})
