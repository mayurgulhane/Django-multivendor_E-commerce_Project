from django.shortcuts import render, redirect, HttpResponse
from app.models import Slider, Banner_area, Main_category, Product, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse


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


def about(request):
    return render(request,'Main/about.html')


def contact(request):
    return render(request,'Main/contact.html')


def product(request):
    category  = Category.objects.all()
    product = Product.objects.all()

    context={
        'category' : category,
        'product' : product
    }

    return render(request,'product/product.html', context)


def filter_data(request):
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')

    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(categories__id__in=categories).distinct()

    if len(brands) > 0:
        allProducts = allProducts.filter(Brand__id__in=brands).distinct()


    t = render_to_string('ajax/product.html', {'product': allProducts})

    return JsonResponse({'data': t})


def productDetail(request,slug):

    productDetail = Product.objects.filter(slug = slug)
    if productDetail.exists():
        productDetail = Product.objects.get(slug = slug)
    else:
        return redirect('error')

    context ={
        'productDetail' : productDetail
    }

    return render(request,'product/product_detail.html',context)


def error(request):
    return render(request,'error/404.html')


def myAccount(request):
    return render(request,'account/my_account.html')


def accountRegister(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username, email, password)

        if User.objects.filter(username = username).exists():
            messages.error(request,"Username is already exists")
            return redirect('login')
        
        if User.objects.filter(email = email).exists():
            messages.error(request,"Email Id  are already exists")
            return redirect('login')

        user = User(
            username = username,
            email = email
        )
        user.set_password(password)
        user.save()
        messages.success(request,"Your Registration Successfully ! Please Login")
        return redirect('login')


    return render(request,'account/my_account.html')

def logIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('home')
        else:
            messages.error(request,"Email and Password Are Invalid !")
            return redirect('login')


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request,'profile/profile.html')


@login_required(login_url='/accounts/login/')
def profileUpdate(request):
    if request.method == "POST":
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        userId = request.user.id

        updateProfile = User.objects.get(id=userId)

        updateProfile.first_name = firstName
        updateProfile.last_name = lastName
        updateProfile.username = username
        updateProfile.email = email

        if password != None and password != "":
            updateProfile.set_password(password)
            
        updateProfile.save()

        messages.success(request,"Your Profile Successfully Updated..")
        return redirect('profile')

    return render(request,'profile/profile.html')