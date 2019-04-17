from django.shortcuts import render, redirect
from . import  models, forms

def signin(request):
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
                    request.session['user_email'] = user.user_email
                    return redirect('/', locals())
                else:
                    message = "密码不正确！"
            except:
                message = "邮箱不存在！"
        return render(request, 'login/signin.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login/signin.html', locals())



def signup(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        signup_form = forms.SignupForm(request.POST)
        message = "请检查填写的内容！"
        if signup_form.is_valid():  # 获取数据
            username = signup_form.cleaned_data['username']
            email = signup_form.cleaned_data['email']
            password1 = signup_form.cleaned_data['password1']
            password2 = signup_form.cleaned_data['password2']
            phone = signup_form.cleaned_data['phone']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/signup.html', locals())
            else:
                same_email_user = models.User.objects.filter(user_email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/signup.html', locals())
                if len(phone) != 11:
                    message = '手机号码错误'
                    return render(request, 'login/signup.html', locals())
                if len(password1) < 6:
                    message = '密码必须不少于六位'
                    return render(request, 'login/signup.html', locals())
                # 当一切都OK的情况下，创建新用户
                userid_query = models.User.objects.values_list('user_id').order_by('user_id').reverse()
                userid_current = userid_query[0][0]
                new_mainpage = models.Mainpage()
                new_mainpage.main_id = userid_current + 1
                new_user = models.User()
                new_user.user_id = userid_current+1
                new_user.user_passwd = password1  # 使用加密密码
                new_user.user_email = email
                new_user.user_name = username
                new_user.user_phone = phone
                new_user.mainpage_main = new_mainpage
                new_user.user_idenity = 0
                new_mainpage.save()
                new_user.save()
                return redirect('/login/signin/',locals())  # 自动跳转到登录页面
    signup_form = forms.SignupForm()
    return render(request, 'login/signup.html',locals())

def logout(request):
    request.session.flush()
    return redirect('/', locals())

def massagepage(request):
    return render(request, 'login/massagepage.html')