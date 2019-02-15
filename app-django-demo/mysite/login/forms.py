from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="userid", max_length=128)
    password = format.CharField(label="userpasswd",max_lenght=256,widget=forms.PasswordInput)