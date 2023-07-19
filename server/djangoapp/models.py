import sys
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()
from django.utils.timezone import now
from django.conf import settings
import uuid

# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100, null=False, default='car_make')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: " + self.name + ',' + \
                "Description: " + self.description


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, default='car_model')
    dealer_id = models.IntegerField()
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    SPORTS_CAR = 'Sports_car'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (SPORTS_CAR, 'Sports_car'),
    ]
    car_type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=False, default=SEDAN)
    year = models.DateField(null=True)

    def __str__(self):
        return "Name: " + self.name + ',' + \
                "Dealer ID: " + self.dealer_id + ',' + \
                "Car Type: " + self.car_type


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
