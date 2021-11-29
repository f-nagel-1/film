from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=60)

class Category(models.Model):
    name = models.CharField(max_length=60)

class Film(models.Model):
    title = models.CharField(max_length=60)
    release_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    available_in_countries = models.ManyToManyField(Country)
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)

class Director(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
