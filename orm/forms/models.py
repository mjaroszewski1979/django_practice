from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Students(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, default='')
    address = models.CharField(max_length=100)
    age = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Students, self).save()



    def __str__(self):
        return self.name
