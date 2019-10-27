from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from .pass_gen import generate


"""
Admin class goes to the admin.py because of the Django's architecture
"""

class InnoFoodUser(AbstractBaseUser):
    name = models.CharField(max_length=100)
    visible = models.BooleanField(default=True)

class Customer(InnoFoodUser):
    address = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=12)

    def create_order(self):
        pass





class Cafe(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=400)
    # manager = models.OneToOneField(Manager, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)

    def delete_cafe(self):
        pass


class Manager(models.Model):
    # Cafe is in brackets because it's the case when two models reference each other (Manager and Cafe)
    assigned_cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    visible = models.BooleanField(default=True)



class Menu(models.Model):
    cafe = models.OneToOneField(Cafe, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)

    def create_dish(self):
        pass


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    visible = models.BooleanField(default=True)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    # manager = models.ForeignKey(Ma)

    def edit_dish(self):
        pass


class OrderDetail(models.Model):
    dishes = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def get_all_dishes(self):
        pass


class Order(models.Model):
    destination = models.CharField(max_length=400)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    parameter = models.OneToOneField(OrderDetail, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)

    def delete_order(self):
        pass

    def cancel_order(self):
        pass

    def create_complaint(self):
        pass

    def confirm_order(self):
        pass


class Complaint(models.Model):
    description = models.TextField(max_length=500)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    complaint_resolved = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)

    def resolve(self):
        pass
