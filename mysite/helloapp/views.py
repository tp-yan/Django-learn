from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 包含了对某个HTTP请求的响应。类似于 controller

# 处理请求的具体函数
def hello(request):
	return HttpResponse("hello,django!")
