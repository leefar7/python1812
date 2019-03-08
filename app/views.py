from django.shortcuts import render

# Create your views here.
from app.models import Wheel, Nav, MustBuy, Shops


def home(request):
    wheel = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuy=MustBuy.objects.all()
    shops= Shops.objects.all()
    data={
             'wheel': wheel,
                'navs': navs,
        'mustbuy':mustbuy,
        'shops':shops,
    }



    return render(request, 'home/home.html',context=data)


def market(request):
    return render(request,'market/market.html')


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):
    return render(request, 'mine/mine.html')