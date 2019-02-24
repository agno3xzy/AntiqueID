from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="邮箱", max_length=128, widget=forms.EmailInput(attrs={'class': 'form-control' ,'aria-describedby':"emailHelp"}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignupForm(forms.Form):
    username = forms.CharField(label="昵称", max_length=45, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="手机号码", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

