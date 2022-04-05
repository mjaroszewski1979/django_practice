from django.urls import path
from . import views

app_name = 'cities'

urlpatterns = [
    path('detail/<slug:slug>/', views.detail, name='detail'),
    path('', views.cities_list, name='cities_data'),
    path('create/<pk>/', views.create_city, name='create-city'),
    path('city_detail/<pk>/', views.detail_city, name='detail-city'),
    path('city_update/<pk>/', views.update_city, name='update-city'),
    path('city_delete/<pk>/', views.delete_city, name='delete-city'),
    path('htmx/city-form', views.create_city_form, name='create-city-form'),
    
]