from django.shortcuts import render
from datetime import datetime

# Create your views here.
def msgproc(request):
	datelist = []
	if request.method == 'POST':
		userA = request.POST.get('userA',None)
		userB = request.POST.get('userB',None)
		msg = request.POST.get('msg',None)
		time = datetime.now()	# 使用后台时间
		with open('msgdata.txt','a+') as f:		# 存放在工程根目录下
			f.write("{}--{}--{}--{}--\n".format(userB,userA,msg,time.strftime("%Y-%m-%d %H:%M:%S")))

	if request.method == "GET":
		userC = request.GET.get("userC",None)
		if userC:
			with open("msgdata.txt","r") as f:
				cnt = 0
				for line in f:
					line_data = line.split('--')
					if line_data[0] == userC:
						cnt += 1
						d = {"userA":line_data[1],"msg":line_data[2],"time":line_data[3]}
						datelist.append(d)
					if cnt >= 10:
						break

	return render(request,"MsgSingleWeb.html",{"data":datelist})	# {"data":datelist} ： 向对应html页面中特定变量赋值