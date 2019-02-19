from django.shortcuts import render, redirect
from . import  models, forms
# Create your views here.

def signin(request):
    if request.session.get('is_login', None):
        message = "重复登陆！"
        return redirect("http://127.0.0.1:8000/classification/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "所有字段都必须填写！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(user_email=username)
                if user.user_passwd == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.user_id
                    request.session['user_id'] = user.user_email
                    return redirect("http://127.0.0.1:8000/classification/")
                    message = "密码正确！"
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"

        #return render(request, 'login/signin.html', {"message": message})
        return render(request, 'login/signin.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login/signin.html', locals())



def signup(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册
        return redirect("/index/")
    if request.method == "POST":
        signup_form = forms.SignupForm(request.POST)
        message = "请检查填写的内容！"
        if signup_form.is_valid():  # 获取数据
            username = signup_form.cleaned_data['username']
            password1 = signup_form.cleaned_data['password1']
            password2 = signup_form.cleaned_data['password2']
            email = signup_form.cleaned_data['email']
            userid = request.POST.get('userid')

            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/signup.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/signup.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/signup.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.id = userid
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    signup_form = forms.SignupForm()
    return render(request, 'login/signup.html')

def massagepage(request):
    return render(request, 'login/massagepage.html')