from django.urls import path
from . import views

app_name = 'forms'

urlpatterns = [
    path('one/', views.index_1, name='index_1'),
    path('two/', views.index_2, name='index_2'),
    path('three/', views.index_3, name='index_3'),
    path('four/', views.index_4, name='index_4'),
    
]