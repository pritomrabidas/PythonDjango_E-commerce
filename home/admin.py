from django.contrib import admin
from .models import *
class SearchProduct(admin.ModelAdmin):
    list_display = ["name", "price", "brand","best_selling","discount",]
    search_fields = ["name", "price", "brand","best_selling","discount",]

admin.site.register(Slider)
admin.site.register(Catagory)
admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Product,SearchProduct)
admin.site.register(Review)
admin.site.register(Cart)
# Register your models here.
