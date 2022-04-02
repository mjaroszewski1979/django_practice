from django.db import models
from django.utils.text import slugify
from django.urls import reverse

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
    slug = models.SlugField(blank=True, default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save()

    def get_absolute_url(self): # < here
        return reverse('cities:detail', args=[str(self.slug)])


    

