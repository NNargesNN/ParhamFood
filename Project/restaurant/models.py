from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Restaurant(models.Model):
    Name = models.CharField(max_length=120)
    Region = models.OneToOneField(Region, on_delete=models.CASCADE)
    Manager = models.OneToOneField(ManagerUser, on_delete=models.CASCADE)
    Address = models.TextField(blank=True, null=True)
    DeliveryCost = models.IntegerField(null=False)
    DeliveryTime = models.IntegerField(null=False)
    ServiceRegions = models.ManyToManyField(Region)


class Food(models.Model):
    Name = models.CharField(max_length=100)
    Status = models.BooleanField(default=True)
    Price = models.IntegerField(null=False)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Review(models.Model):
    User = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Text = models.CharField(max_length=140)
    Vote = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    ManagerResponse = models.CharField(max_length=140)

