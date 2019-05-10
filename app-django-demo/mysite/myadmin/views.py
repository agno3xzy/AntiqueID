from django.shortcuts import render, redirect
import login.models as models

# Create your views here.
def index(request):
    return render(request, 'myadmin/intro.html')

#用户点击申请专家
def expertapply(request):
    #user_identity为1表示正在审核
    expertList = models.User.objects.filter(user_identity = 1)
    return render(request, 'myadmin/expertapply.html', locals())

#管理员端确认是否通过申请
def checkapply(request):
    if request.method == 'POST':
        UserId = request.POST.get('id')
        operation = request.POST.get('operation')
        if operation == 'pass':
            user = models.User.objects.get(user_id = UserId)
            user.user_identity = 2
            user.save()
        return redirect('/myadmin/expertapply/', locals())

def auctionmanagement(request):
    return render(request, 'myadmin/auctionmanagement.html')

def mallmanagement(request):
    return render(request, 'myadmin/mallmanagement.html')

def usermanagement(request):
    return render(request, 'myadmin/usermanagement.html')

def expert_detail(request):
    return render(request, 'myadmin/expert_detail.html')
