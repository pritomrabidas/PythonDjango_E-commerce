from django.db import models
from django.contrib.auth.models import AbstractUser

class costom_user(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile_images/', default='default.jpg')
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # otp = models.CharField(max_length=6, blank=True, null=True)


    def _str__(self):
        return self.username


