from django.db import models

class BaseClass(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name

class Country(BaseClass):
    created = models.DateTimeField(auto_now_add=True)

class City(BaseClass):
    population = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    

