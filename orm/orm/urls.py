import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls', namespace='student')),
    path('city/', include('cities.urls', namespace='city')),
    path('products/', include('products.urls', namespace='products')),
    path('forms/', include('forms.urls', namespace='forms')),
    path('__debug__/', include(debug_toolbar.urls)),
]
