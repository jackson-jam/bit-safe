import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from blog.models import Products
from blog.models import User
import hashlib


# Create your views here.

def hello(request):
    return HttpResponse('Hello,world')


def index(request):
    view_list = ["123", "123", "123"]
    return render(request, 'index.html', {"view_list": view_list})


def test1(request):
    return render(request, 'bootstrap_test.html')


def info_list(request):
    # 1.获取数据库中用户的所有信息，此处使用products商品类代替用户信息(name-prod_name) (password-prod_price) (age-prod_desc)
    data_list = Products.objects.all()  # select * from products
    print(data_list)

    return render(request, "info_list.html", {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, 'info_add.html')
    # 获取用户提交的信息
    prod_name = request.POST.get("prod_name")
    prod_price = request.POST.get("prod_price")
    prod_desc = request.POST.get("prod_desc")
    # 将获取到到数据添加到数据库
    Products.objects.create(prod_name=prod_name, prod_price=prod_price, prod_desc=prod_desc)

    # return HttpResponse("添加成功")
    # 添加成功后直接跳转到info_list界面
    return redirect("http://127.0.0.1:8000/info/list")  # 跳转到外链页面时需要把http协议和域名整体写全跳转到自己的界面可直接使用/info/list


def info_delete(request):
    nid = request.GET.get('nid')
    Products.objects.filter(id=nid).delete()
    return redirect("http://127.0.0.1:8000/info/list")


def depart_list(request):
    return render(request, 'depart_list.html')


def echarts_list(request):
    return render(request, 'echarts_test.html')


def root(request):
    # return HttpResponse("helloworld!")
    return render(request, 'root.html')


def miniprogram(request):
    return render(request, "miniprogram.html")


def css_test(request):
    return render(request, "account_test.html")


def login(request):
    return render(request, 'login.html')


def user1(request):
    return render(request, 'user.html')


def first(request):
    return render(request, 'first.html')


def first_test(request):
    return render(request, 'first_test.html')


def sign_up(request):
    if request.method == "GET":
        return render(request, 'login.html')
    # 获取用户提交的信息
    user_name = request.POST.get("user_name")
    user_password1 = request.POST.get("user_password_1")
    user_password2 = request.POST.get("user_password_2")
    user_email = request.POST.get("user_email")
    # 对用户密码进行加密
    if user_password1 == user_password2:
        m = hashlib.md5()
        m.update(user_password1.encode())
        password_m = m.hexdigest()
        # 将获取到到数据添加到数据库
        User.objects.create(user_name=user_name, user_password=password_m, user_email=user_email)
        # 添加成功后跳转到首页界面
        return redirect("http://127.0.0.1:8000/first")
    else:
        return HttpResponse("两次输入不一致")


def user_list(request):
    # 1.获取数据库中用户的所有信息，此处使用products商品类代替用户信息(name-prod_name) (password-prod_price) (age-prod_desc)
    data_list = User.objects.all()
    print(data_list)

    return render(request, "user_list.html", {"data_list": data_list})


# def data(request):
#     data_list = scapy_exp.packet
#     print(data_list)
#     return HttpResponse(data_list)
