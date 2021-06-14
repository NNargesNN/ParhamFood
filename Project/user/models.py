from django.contrib.auth.models import User
from django.db import models
from Project.restaurant.models import Food


class Region(models.Model):
    Region = models.IntegerField(null=False)


class CustomerUser(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)


class ManagerUser(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    class OrderState(models.TextChoices):
        AWAITING_APPROVAL = 'AWAITING_APPROVAL'
        PREPARING = 'PREPARING'
        SENDING = 'SENDING'
        DELIVERED = 'DELIVERED'

    User = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    Food = models.ManyToManyField(Food)
    OrderCost = models.IntegerField(null=False)
    ApproximateArrivalTime = models.DateTimeField()
    state = models.CharField(choices=OrderState.choices, max_length=100)

    def add_food_to_order(self, Foods):
        for food in Foods:
            self.Food.add(food)
            self.OrderCost += food.Price
