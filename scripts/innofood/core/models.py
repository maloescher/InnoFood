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
    address = models.TextField(max_length=400)
    phone_number = models.TextField(max_length=12)

    def create_order(self):
        pass


# class Manager(models.Model):
#     # Cafe is in brackets because it's the case when two models reference each other (Manager and Cafe)
#     assigned_cafe = models.OneToOneField('Cafe', on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     visible = models.BooleanField(default=True)

#     def set_cafe(self):
#         pass

#     def delete_manager(self):
#         pass


class Cafe(models.Model):
    name = models.TextField(max_length=100)
    location = models.TextField(max_length=400)
    # manager = models.OneToOneField(Manager, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)

    def delete_cafe(self):
        pass





class ManagerManager(BaseUserManager):
    def create_user(self, email, name, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name = name,
            email=self.normalize_email(email),
        )

        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """

        password = generate()
        print('PASSWORD:', password)

        user = self.create_user(
            email,
            name,
            password=password,
            # date_of_birth=date_of_birth,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class Manager(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=100)
    cafe = models.OneToOneField(Cafe, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Assigned cafe')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = ManagerManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return True









class Menu(models.Model):
    cafe = models.OneToOneField(Cafe, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)

    def create_dish(self):
        pass


class Dish(models.Model):
    name = models.TextField(max_length=100)
    price = models.FloatField(default=0)
    visible = models.BooleanField(default=True)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    # manager = models.ForeignKey(Ma)

    def edit_dish(self):
        pass


class OrderDetail(models.Model):
    dishes = models.OneToOneField(Dish, on_delete=models.CASCADE)

    def get_all_dishes(self):
        pass


class Order(models.Model):
    destination = models.TextField(max_length=400)
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
