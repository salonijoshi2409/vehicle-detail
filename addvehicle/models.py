from wsgiref.validate import validator
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Vechicle(models.Model):
    name = models.CharField(max_length=100)
    speed = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)])
    avgspeed = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)])
    fuellev = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    enginestat = models.CharField(max_length=100)
    temp = models.FloatField()
    on_off = models.BooleanField(default=False)
