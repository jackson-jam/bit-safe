"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
# from blog import views
from django.urls import path
from blog import views
from . import testdb, search, search2
from django.views.static import serve
from django.conf import settings
from user import views as user_views
from machine_l import views as m_views

urlpatterns = [
    #path('', views.root),
    path('', views.first_test),
    path('miniprogram', views.miniprogram),
    path('login', views.login),
    path('sign/up', views.sign_up),
    path('first', views.first),
    path('user/list', views.user_list),
    path('css/test', views.css_test),
    path('admin/', admin.site.urls),
    path('index', views.hello),
    path('hello', views.index),
    path('user1', views.user1),

    # path('runoob/', views.runoob),
    # path('testdb/', testdb.testdb),
    path('search/', search.search),
    path('search_form/', search.search_form),
    path('search_post/', search2.search_post),
    path('test/', views.test1),
    path('data/', m_views.data),
    # 商品管理测试
    path('info/list/', views.info_list),
    path('info/add/', views.info_add),
    path('info/delete/', views.info_delete),
    path('depart/list', views.depart_list),
    path('echarts/list', views.echarts_list),
    path('user/', user_views.user_search,name='user_search'),

    # re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # path('', views.index, name='index'),
]
# handler400 = views.bad_request#配置http400错误界面为bad_request
# handler403 = views.permission_denied
# handler404 = views.page_not_found
# handler500 = views.page_error
