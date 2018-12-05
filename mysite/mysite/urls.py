"""mysite URL Configuration

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
from django.urls import include,path	# include函数专门用于引用其他路由文件

from helloapp import views

#此文件是 工程的全局路由文件

# 路由：将URL请求与处理函数相关联. 与 routes.rb类似
# 一个URL对应一个回调函数
urlpatterns = [
	path('index2/',include('hello2app.urls')),	# 将本地路由加入到 全局路由
	path('index/',views.hello),		# 此处将 index/ 这个URL请求用 view模块的hello函数来处理
    path('admin/', admin.site.urls),
]
