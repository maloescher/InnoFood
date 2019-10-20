from django.contrib import admin
from .models import Cafe, Dish, Complaint, Order, Manager
from django.db import models
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group


class Admin(admin.ModelAdmin):
    def create_cafe(self):
        pass

    def create_manager(self):
        pass


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Manager
        fields = ('email', 'name')

    # def clean_password2(self):
    #     # Check that the two password entries match
    #     # password1 = self.cleaned_data.get("password1")
    #     # password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        # user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Manager
        fields = ('email', 'name', 'cafe')

    # def clean_password(self):
    #     # Regardless of what the user provides, return the initial value.
    #     # This is done here, rather than on the field, because the
    #     # field does not have access to the initial value
    #     return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'cafe')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'name')}),
        ('Job', {'fields': ('cafe',)}),
        # ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'cafe')}
        ),
    )
    search_fields = ('email', 'name', 'cafe')
    ordering = ('email', 'name')
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(Manager, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)


# class ManagerAdmin(admin.ModelAdmin):
    
#     def create_user(self, email=None, password=None, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         now = timezone.now()
#         if not email:
#             raise ValueError('The given email must be set')
#         email = CustomUserManager.normalize_email(email)
#         user = self.model(
#                             username=username, 
#                             email=email,
#                             is_staff=True, 
#                             is_active=True, 
#                             is_superuser=True,
#                             last_login=now, 
#                             date_joined=now, 

#                             assigned_cafe = None,
#                             visible = False
#                             **extra_fields
#                             )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user


#     def set_cafe(self, cafe):
#         self.model.assigned_cafe = cafe

#     def delete(self):
#         visible = False

#     def get_queryset(self, request):
#         qs = super(Manager, self).get_queryset(request) 
#         # qs = Dish.get_queryset()
#         return qs.filter(cafe=self.model.assigned_cafe)

# admin.site.register(Manager, Admin)
# admin.site.register(Manager)
# admin.site.register(Cafe, Admin)
# admin.site.register(Dish)
# admin.site.register(Order)
# admin.site.register(Complaint)




