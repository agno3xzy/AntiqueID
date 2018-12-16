from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myadmin/intro.html')

def expertapply(request):
    return render(request, 'myadmin/expertapply.html')

def auctionmanagement(request):
    return render(request, 'myadmin/auctionmanagement.html')

def mallmanagement(request):
    return render(request, 'myadmin/mallmanagement.html')

def usermanagement(request):
    return render(request, 'myadmin/usermanagement.html')

def expert_detail(request):
    return render(request, 'myadmin/expert_detail.html')
