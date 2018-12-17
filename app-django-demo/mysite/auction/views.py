from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'auction/auction.html')

def details(request):
    return render(request, 'auction/auction_details.html')