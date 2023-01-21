from django.contrib import admin
from .models import *

# Register your models here.

class Product_Image(admin.TabularInline):
    model = Product_image

class Additional_Information(admin.TabularInline):
    model = Additional_information

class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Image, Additional_Information)
    list_display = ('product_name','price','categories','section')
    list_editable = ('categories','section')

 
admin.site.register(Product, Product_Admin)
admin.site.register((Product_image, Additional_information, Section))
admin.site.register((Slider,Banner_area))
admin.site.register((Main_category, Category, Sub_category))
