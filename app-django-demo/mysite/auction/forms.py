from django import forms


class PirceForm(forms.Form):
    userpirce = forms.CharField(label="用户报价", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
