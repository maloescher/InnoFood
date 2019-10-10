from django.db import models
from django.contrib.auth.models import User


"""
Admin class goes to the admin.py because of the Django's architecture
"""


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address = models.TextField(max_length=400)
    phone_number = models.TextField(max_length=12)

    def create_order(self):
        pass


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Cafe is in brackets because it's the case when two models reference each other (Manager and Cafe)
    assigned_cafe = models.OneToOneField('Cafe', on_delete=models.CASCADE)

    def set_cafe(self):
        pass

    def delete_manager(self):
        pass


class Cafe(models.Model):
    id = models.Index()
    name = models.TextField(max_length=100)
    location = models.TextField(max_length=400)
    manager = models.OneToOneField(Manager, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)

    def delete_cafe(self):
        pass


class Menu(models.Model):
    id = models.Index()
    cafe = models.OneToOneField(Cafe, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)

    def create_dish(self):
        pass


class Dish(models.Model):
    id = models.Index()
    name = models.TextField(max_length=100)
    price = models.FloatField(default=0)
    visible = models.BooleanField(default=True)

    def edit_dish(self):
        pass


class OrderDetail(models.Model):
    dishes = models.OneToOneField(Dish, on_delete=models.CASCADE)

    def get_all_dishes(self):
        pass


class Order(models.Model):
    destination = models.TextField(max_length=400)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
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
    id = models.Index()
    description = models.TextField(max_length=500)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    complaint_resolved = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)

    def resolve(self):
        pass
