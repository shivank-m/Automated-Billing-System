from typing import AnyStr
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import CustomerDetails
from inventory.models import UserCart, ItemMain
import json
from django.contrib.auth.decorators import login_required

# Create your views here.


def customer_details(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            first_name = request.POST['first_name']
            middle_name = request.POST['middle_name']
            last_name = request.POST['last_name']
            state = request.POST['state']
            street = request.POST['street']
            city = request.POST['city']
            phone = request.POST['phone']
            email = request.POST['email']
            billing = CustomerDetails.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name,
                                                     state=state, street=street, city=city, phone=float(phone), email=email)
            billing.save()
            return redirect('homepage')
        else:
            return redirect('login')
    else:
        return render(request, 'checkout/customer details.html', {})


def generate_bill(request):
    context = {}
    customer = list(CustomerDetails.objects.all())[-1]
    context['customer'] = customer
    unique_items1 = []
    unique_items2 = []
    total_amount = 0
    if request.method == "GET":
        user = request.user
        items = UserCart.objects.filter(
            user=User.objects.filter(username=user)[0]
        )
        l = []
        for i in items:
            ll = []
            item = ItemMain.objects.filter(slug=i.itemid)[0]
            print(item)
            if item.itemid in unique_items1:
                pass
            else:
                ll.append(item.itemname)
                unique_items1.append(item.itemid)
            price = item.price
            discount = item.discount
            newPrice = price - (price * discount)/100
            if item.itemid in unique_items2:
                pass
            else:
                ll.append(newPrice)
                ll.append(i.quantity)
                unique_items2.append(item.itemid)
                l.append(ll)
            total_amount += newPrice
        print(l)
        context['items'] = l
        context['total'] = total_amount
    return render(request, "checkout/bill.html", context)
