from modulefinder import Module

from django.db import models

# Create your models here.
class Students(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name