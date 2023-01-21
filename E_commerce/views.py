from django.shortcuts import render
from app.models import Slider, Banner_area, Main_category, Product


def Home(request):
    slider = Slider.objects.all().order_by('-id')[0:3]

    banner = Banner_area.objects.all().order_by('-id')[0:3]

    mainCategory = Main_category.objects.all()

    topDeals = Product.objects.filter(section__name = "Top Deals Of The Day")

    context = {
        'slider' : slider,
        'banner' : banner,
        'mainCategory' : mainCategory,
        'topDeals' : topDeals
    }

    return render(request,'Main/Home.html',context)