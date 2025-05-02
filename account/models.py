from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_images/', default='default.jpg')
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    otp = models.CharField(max_length=4, blank=True, null=True)

    def _str__(self):
        return self.username


