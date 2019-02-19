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
                    request.session['user_email'] = user.user_email
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
    return render(request, 'login/signup.html')

def massagepage(request):
    return render(request, 'login/massagepage.html')