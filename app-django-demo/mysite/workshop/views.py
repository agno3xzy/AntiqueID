from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'workshop/frontpage.html')

def allcomment(request):
    return render(request, 'workshop/all_comments.html')

def allexpert(request):
    return render(request, 'workshop/all_experts.html')