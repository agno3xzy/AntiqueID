from django.shortcuts import render, redirect
from . import  models
# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        print(username)
        print(password)
        print('------------------')
        if username.strip() and password.strip():  # 确保用户名和密码都不为空
            username = str(username)
            password = str(password)
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(user_email=username)
                print(user.user_passwd)
                print(password)
                print('------------------')
                if user.user_passwd == password:

                    message = "密码正确！"
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login/signin.html', {"message": message})
    return render(request, 'login/signin.html')


def signup(request):
    return render(request, 'login/signup.html')

def massagepage(request):
    return render(request, 'login/massagepage.html')