from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save

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
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("productDetail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app_Product"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Product)

    
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
