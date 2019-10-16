from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def landing_page(request):
    return render(request, "landing.html")


@login_required
def customer_page(request):
    return render(request, "customer.html")