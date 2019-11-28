from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

# this function is connected to use case  016 SignUp
# this function is connected to use case  017 Sign in
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    # class Meta:
    #     model = settings.AUTH_USER_MODEL
    #     fields = ["username", "email", "password"]


# this function is connected to use case  007 Create Order
class ComplaintForm(forms.Form):
    order = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
