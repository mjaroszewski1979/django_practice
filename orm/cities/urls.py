from django.urls import path
from . import views

app_name = 'cities'

urlpatterns = [
    path('detail/<slug:slug>/', views.detail, name='detail'),
    path('', views.cities_list, name='cities_data'),
    
]