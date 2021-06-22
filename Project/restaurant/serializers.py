from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework import serializers
from .models import Restaurant, Food, Review


class RestaurantSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(max_length=120)
    Region = serializers.OneToOneField(Region, on_delete=models.CASCADE)
    Manager = serializers.OneToOneField(ManagerUser, on_delete=models.CASCADE)
    Address = serializers.TextField(blank=True, null=True)
    DeliveryCost = serializers.IntegerField(null=False)
    DeliveryTime = serializers.IntegerField(null=False)
    ServiceRegions = serializers.ManyToManyField(Region)

    class Meta:
        model = Restaurant
        fields = '__all__'

    def createRestaurant(self, data):
        currentUser = self.M

    def menu(self, obj):
        allFoods = Food.objects.filter(Restaurant=obj)


class FoodSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=100)
    Status = serializers.BooleanField(default=True)
    Price = serializers.IntegerField(null=False)
    Restaurant = serializers.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        model = Food


class Review(serializers.Serializer):
    User = serializers.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    Order = serializers.ForeignKey(Order, on_delete=models.CASCADE)
    Text = serializers.CharField(max_length=140)
    Vote = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    ManagerResponse = serializers.CharField(max_length=140)

    class Meta:
        model = Review
