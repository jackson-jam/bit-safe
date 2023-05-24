from django.http import HttpResponse
from django.shortcuts import render
from blog.models import User


# 表单
def search_form(request):
    return render(request, 'search_form.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        if request.GET['q'] not in User.user_name:
            message = 'cannot search'
        else:
            message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)