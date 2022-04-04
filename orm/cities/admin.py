from django.contrib import admin

from . import models

class CityInlineAdmin(admin.TabularInline):
    model = models.City

class CountryAdmin(admin.ModelAdmin):
    inlines = [CityInlineAdmin]

admin.site.register(models.Country)
admin.site.register(models.City)
