from datetime import date
from django.db import models

# Create your models here.

class Maindishes(models.Model):
    foodname = models.CharField(max_length=50)
    
class Sidedishes(models.Model):
    maindishes = models.ForeignKey(Maindishes, on_delete=models.CASCADE)
    foodname = models.CharField(max_length=50)
    
class Desserts(models.Model):
    maindishes = models.ForeignKey(Maindishes, on_delete=models.CASCADE)
    foodname = models.CharField(max_length=50)
    
class revenue(models.Model):
    maindishes = models.ForeignKey(Maindishes, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
