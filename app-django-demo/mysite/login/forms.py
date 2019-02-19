from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.EmailInput(attrs={'class': 'form-control' ,'aria-describedby':"emailHelp"}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignupForm(forms.Form):
    user_id = forms.IntegerField(primary_key=True, auto_created=True, unique=True)
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
