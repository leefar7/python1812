import hashlib
import random
import time

from django.core.cache import cache
from django.shortcuts import render, redirect

# Create your views here.


from app.models import Wheel, Nav, MustBuy, Shops, Mainshow, Foodtype, Goods, User


def home(request):
    # 轮播图
    wheel = Wheel.objects.all()
    # 导航
    navs = Nav.objects.all()
    # 每日必购
    mustbuys=MustBuy.objects.all()
    # 商品部分
    shops= Shops.objects.all()
    shophead = shops[0]
    shoptabs=shops[1:3]
    shopclass_list = shops[3:7]
    shopcommend_list=shops[7:11]


    mianshows = Mainshow.objects.all()

    data={
             'wheel': wheel,
                'navs': navs,
        'mustbuys':mustbuys,
        'shops':shops,
        'shophead':shophead,
        'shoptabs':shoptabs,
        'shopclass_list':shopclass_list,
        'shopcommend_list':shopcommend_list,
        'mainshows':mianshows,
    }



    return render(request, 'home/home.html',context=data)


# def market(request,categoryid=104749):
def market(request):
    foodtypes = Foodtype.objects.all()
    # goods_list = Goods.objects.all()[0:5]
    # 默认打开热销榜
    # 客户端 需要记录点击分类的下标
    index = int(request.COOKIES.get('index','0'))
    # 根据index 获取对应的分类ID
    categoryid=foodtypes[index].typeid
    # 根据分类ID 获取对应分类信息
    goods_list = Goods.objects.filter(categoryid=categoryid)

    # 获取子类信息
    childtypenames=foodtypes[index].childtypenames
    #将对应的子类拆分
    childtype_list=[]
    for item in childtypenames.split('#'):
        item_arr=item.split(':')
        temp_dir={
            'name':item_arr[0],
            'id':item_arr[1]
        }
        childtype_list.append(temp_dir)

    data={
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'childtype_list': childtype_list
    }
    return render(request,'market/market.html',context=data)


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):
    token=request.session.get('token')
    userid = cache.get(token)
    user=None
    if userid:

        user = User.objects.get(pk=userid)
    return render(request, 'mine/mine.html',context={'user':user})


def login(request):
    return render(request,'mine/login.html')


def generate_password(param):
    md5=hashlib.md5()
    md5.update(param.encode('utf-8'))
    return md5.hexdigest()

def generate_token():
    temp =str(time.time())+str(random.random())
    md5=hashlib.md5()
    md5.update(temp.encode('utf-8'))
    return md5.hexdigest()


def register(request):
    if request.method=='GET':

        return render(request, 'mine/register.html')
    elif request.method=='POST':
        email =request.POST.get('email')
        name =request.POST.get('name')
        password =generate_password(request.POST.get('password'))

        # 存入数据库
        user = User()
        user.email=email
        user.password=password
        user.name=name
        user.save()
        token=generate_token()
        cache.set(token,user.id,60*60*24*3)
        request.session['token']=token



        return redirect('axf:mine')


def logout(request):
    request.session.flush()
    return redirect('axf:mine')