"""innofood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import core.views

urlpatterns = [
    path('welcome/', core.views.landing_page, name='landing'),

    # CUSTOMER PART
    path('cafes/', core.views.customer_page, name='cafes'),
    # path('dishes/', ..., name='customer_dishes'),
    # path('orders/', ..., name='customer_orders'),
    # path('complaint/', ..., name='customer_new_complaint'),
    # path('cart/', ..., name='customer_cart'),
    # path('order/', ..., name='customer_order'),
    # path('account/', ..., name='customer_account'),
    # path('complaints/', ..., name='customer_complaints'),

    # MANAGER PART
    # path('manager/orders/<status:str>', ..., name='manager_orders')
    # path('manager/complaints/<status:bool>', ..., name='manager_complaints')

    # ADMIN PART
    # path('admin/cafes/', ..., name='admin_cafes')
    # path('admin/managers/', ..., name='admin_managers')

    path('admin/', admin.site.urls),

]
