from django.contrib import admin
from .models import ItemMain, ItemsCat, Contact, UserCart

# Register your models here.
admin.site.register(ItemMain)
admin.site.register(ItemsCat)
admin.site.register(Contact)
admin.site.register(UserCart)
