from django.db import models

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     slug = models.SlugField(max_length=120, unique=True)

# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=220, unique=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     available = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     image = models.ImageField(upload_to='products/', blank=True, null=True)
#     def __str__(self):
#         return self.name