from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def index(request):
    return render(request, 'auction/auction.html')


def details(request):
    userprice = 'wrong'
    if request.method == "POST":
        price_form = forms.PirceForm(request.POST)
        if price_form.is_valid():
            userprice = price_form.cleaned_data['userpirce']
            return render(request, 'auction/auction_details.html',locals())
    price_form = forms.PirceForm()
    return render(request, 'auction/auction_details.html',locals())

