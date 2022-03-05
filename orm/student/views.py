from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q



def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def student_list(request):
    context = {}
    all_studs = Student.objects.all()
    context['all'] = all_studs
    # Filter for students with surnames starting with and not starting with...
    context['data'] = Student.objects.filter(Q(surname__endswith='ski') & ~Q (surname__startswith='jaro'))
    # Filter for students with surnames starting with or starting with...
    context['data1'] = Student.objects.filter(surname__startswith='jaroszewski') | Student.objects.filter(surname__startswith='kowalski')
    context['data2'] = Student.objects.all()
    context['data3'] = Student.objects.filter(Q(age__gt=30) & Q(age__lt=40))
    context['data4'] = all_studs.exclude(Q(firstname__endswith='ej') & ~Q (classroom=2))
    # Performing union of list values - students first names and teachers first names - must be same model field to work
    context['union'] = Student.objects.all().values_list('firstname').union(Teacher.objects.all().values_list('firstname'))
    # Performing union of values - students first names and teachers first names
    context['union_dict'] = Student.objects.all().values('firstname').union(Teacher.objects.all().values('firstname'))
    # Filter for students surname endswith ski and returning only their surnames
    context['only'] = Student.objects.filter(Q(surname__endswith='ski')).only('surname')
    # Raw sql querries
    context['raw'] = Teacher.objects.raw("SELECT * FROM student_student")

    '''cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM student_teacher")
    context['counter'] = cursor.fetchone()'''
    # Using cursor object to perform sql query and returnig dictionary as a result
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student_student")
    context['dict'] = dictfetchall(cursor)


    print(context['data'].query)
    print(connection.queries)

    return render(request, 'index.html',{'context': context})
