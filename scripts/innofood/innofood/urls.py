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
import core.views as views
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    # CUSTOMER PART
    path('cafes/', views.CafeListView.as_view(), name='cafes'),
    path('cafes/<int:id>/', views.DishListView.as_view(), name='dishes'),
    # path('orders/', ..., name='customer_orders'),
    # path('complaint/', ..., name='customer_new_complaint'),
    path('cart/', views.CartListView.as_view(), name='cart'),
    path('create_order/', views.create_order, name='new_order'),
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
