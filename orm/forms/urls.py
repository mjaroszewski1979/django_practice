from django.urls import path
from . import views

app_name = 'forms'

urlpatterns = [
    path('one/', views.index_1, name='index_1'),
    path('two/', views.index_2, name='index_2'),
    path('three/', views.index_3, name='index_3'),
    path('four/', views.index_4, name='index_4'),
    path('five/', views.index_5, name='index_5'),
    path('six/', views.index_6, name='index_6'),
    path('seven/', views.index_7, name='index_7'),
    path('create/', views.CreateView.as_view(), name='create_view'),
    path('newcreate/', views.NewCreateView.as_view(), name='new_create_view'),

    
]