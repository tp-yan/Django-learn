"""cloudms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
	path('msggate/',include('msgapp.urls')),	# URL逐一匹配，不考虑HTTP请求方式，只根据URL进行路由
    path('admin/', admin.site.urls),	# path(route--string,view)处理字符串路由，repath(route--regx,view)处理正则表达式路由
    # route的三种表现形式：
    # 1.精确字符串： articles/2003
    # 2.Django的转换格式（一个URL模板）匹配URL同时获得URL路径信息：<类型:变量名> 类型：str（默认），int,slug,uuid,path. 目的：提取URL路径上的参数，可将参数传递给后面的处理函数
    # 3.正则表达式： articles/(?P<year>[0-9]{4})/  : 正则表达式也可以提取URL参数但只能是str类型
]
