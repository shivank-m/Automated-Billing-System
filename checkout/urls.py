from django.urls import path
from . import views

urlpatterns = [
    path("customer_details/", views.customer_details, name="customer_details"),
    path("bill/", views.generate_bill, name="bill")
]
