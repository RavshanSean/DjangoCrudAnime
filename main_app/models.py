from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Weapon(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('weapon-detail', kwargs={'pk': self.id})


class Ninja(models.Model):
    name = models.CharField(max_length=100)
    clan = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    chakra = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weapons = models.ManyToManyField(Weapon)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ninja-detail', kwargs={'ninja_id': self.id})

class Meta:
    ordering = ['-date']
