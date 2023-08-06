from django.db import models

# Create your models here.


class CustomerDetails(models.Model):
    first_name = models.CharField(max_length=264)
    middle_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    street = models.CharField(max_length=264)
    state = models.CharField(max_length=264)
    city = models.CharField(max_length=264)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=264)
