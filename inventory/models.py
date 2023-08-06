from statistics import mode
from django.db import models
from django.conf import settings
from django.db.models.base import Model
from django.utils.text import slugify
from django.contrib.auth.models import User

# # Create your models here.


class ItemsCat(models.Model):
    catName = models.CharField(max_length=20, default="")

    def __str__(self) -> str:
        return self.catName


class ItemMain(models.Model):
    itemid = models.AutoField(primary_key=True)
    itemname = models.CharField(max_length=50)
    discount = models.DecimalField(decimal_places=2, max_digits=25)
    price = models.DecimalField(decimal_places=2, max_digits=25)
    type = models.ForeignKey(ItemsCat, on_delete=models.CASCADE)
    composition = models.TextField()
    manufacturingdate = models.DateField()
    expirydate = models.DateField()
    quantity = models.DecimalField(decimal_places=2, max_digits=25, default=0)
    slug = models.SlugField(max_length=50, unique=True,
                            default="", editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.itemid, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.itemid)

    def update_quantity(self, quantity):
        print(self.quantity)
        self.quantity = self.quantity + quantity
        print(self.quantity)
        return self.quantity


class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itemid = models.ForeignKey(ItemMain, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(str(self.user) + " -> " + str(self.itemid))


class Contact(models.Model):
    username = models.CharField(max_length=264)
    phone = models.IntegerField(default=0)
    problem = models.CharField(max_length=1264)
