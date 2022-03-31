from django.shortcuts import render

from . import forms

def index_1(request):
    context = {'form': forms.CollegeForm()}
    return render(request, 'forms/index_1.html', context)

def index_2(request):
    context = {'form': forms.UniversityForm()}
    return render(request, 'forms/index_2.html', context)

def index_3(request):
    context = {'form': forms.SchoolForm()}
    return render(request, 'forms/index_3.html', context)

def index_4(request):
    context = {'form': forms.NewSchoolForm()}
    return render(request, 'forms/index_4.html', context)
