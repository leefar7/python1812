from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home/home.html')


def home(request):
    return render(request, 'home/home.html')


def market(request):
    return render(request,'market/market.html')