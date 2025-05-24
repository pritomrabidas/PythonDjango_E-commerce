from django.db import models

# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to='slider_images/')

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=100)
    # slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
class Brand(models.Model):
    name = models.CharField(max_length=100)
    # slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
     
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sku = models.CharField(max_length=100, unique=True)
    tags = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='profile_images/',default='default.jpg',null=True,blank=True)
    ex_image1 = models.ImageField(upload_to='profile_images/',default='default.jpg',null=True,blank=True)
    ex_image2 = models.ImageField(upload_to='profile_images/',default='default.jpg',null=True,blank=True)
    ex_image3 = models.ImageField(upload_to='profile_images/',default='default.jpg',null=True,blank=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    condition = models.CharField(max_length=100 , choices=[('new', 'New'), ('sale', 'sale'), ])
    new_arrival = models.BooleanField(default=False)
    top_rated = models.BooleanField(default=False)
    best_selling = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    rating = models.IntegerField()

    def _str_(self):
        return f"{self.user} - {self.product.name} - {self.rating}"