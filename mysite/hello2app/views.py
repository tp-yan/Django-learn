from django.shortcuts import render


# Create your views here.
def hello(request):
	return render(request,"first.html")	# 第二个参数 是返回html的名字