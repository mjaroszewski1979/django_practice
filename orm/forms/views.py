from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CityForm

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

def index_5(request):
    context = {'form': forms.InlineForm()}
    return render(request, 'forms/index_5.html', context)

class CreateView(SuccessMessageMixin, generic.CreateView):
    template_name = 'forms/create.html'
    success_message = 'Success'
    form_class = CityForm
