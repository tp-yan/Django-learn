
from django.urls import path
from . import views		# . 指当前app
# 此文件是 hello2app下的本地路由文件，需要加到全局urls中

urlpatterns = [
	path('',views.hello), 
]
