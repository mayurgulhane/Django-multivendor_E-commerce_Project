from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Slider(models.Model):
    Discount_Deal = (
        ('HOT DEALS','HOT DEALS'),
        ('New Arraivels','New Arraivels'),
    )

    image = models.ImageField(upload_to='media/slider_img')
    discount_deal = models.CharField(choices= Discount_Deal, max_length=100)
    sale = models.IntegerField()
    brand_name = models.CharField(max_length=200)
    discount = models.IntegerField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name


class Banner_area(models.Model):
    image = models.ImageField(upload_to='media/banner_img')
    discount_deal = models.CharField(max_length=100)
    quote = models.CharField(max_length=100)
    discount = models.IntegerField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.quote


class Main_category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    main_category = models.ForeignKey(Main_category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " -- " + self.main_category.name


class Sub_category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.category.main_category.name + " -- " + self.category.name + " --- " + self.name


class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    total_quantity = models.IntegerField()
    availability = models.IntegerField()
    featured_image = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    product_info = RichTextField()
    model_name = models.CharField(max_length=100)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.CharField(max_length=100)
    description = RichTextField()
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product_name
    

class Product_image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.product.product_name


class Additional_information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)

    def __str__(self):
        return self.product.product_name
