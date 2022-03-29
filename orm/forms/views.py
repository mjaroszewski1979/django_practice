from django.shortcuts import render

from .forms import UniversityForm

def index(request):
    context = {'form': UniversityForm()}
    return render(request, 'forms/index.html', context)
