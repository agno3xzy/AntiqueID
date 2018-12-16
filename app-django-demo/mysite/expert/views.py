from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'expert/expert_choose.html')

def detail(request):
    return render(request, 'expert/expert_detail.html')

def comment(request):
    return render(request, 'expert/expert_comment.html')

def comment_detail(request):
    return render(request, 'expert/expert_comment_detail.html')