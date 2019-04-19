from django.shortcuts import render, redirect
from . import forms
import login.models as models

comm_collection_id = []
expert_collection_id = []
comm_collection_num = 0
expert_collection_num = 0
def collection(Mainpage):
    comm_collection = Mainpage.main_collection
    expert_collection = Mainpage.main_followexpert
    global comm_collection_id
    comm_collection_id = []
    global expert_collection_id
    expert_collection_id = []
    global comm_collection_num
    comm_collection_num = 0
    global expert_collection_num
    expert_collection_num = 0
    str = ""
    for i in comm_collection:
        if i == '#':
            comm_collection_id.append(models.Commodity.objects.get(comm_id = int(str)))
            comm_collection_num = comm_collection_num + 1
            str = ""
        else:
            str = str + i
    for i in expert_collection:
        if i == '#':
            expert_collection_id.append(models.Expert.objects.get(expert_id = int(str)))
            expert_collection_num = expert_collection_num + 1
            str = ""
        else:
            str = str + i


def index(request):
    if request.session.get('is_login', None):
        user_id = request.session['user_id']
        user = models.User.objects.get(user_id = user_id)
        mainpage_id = user.mainpage_main.main_id
        Mainpage = models.Mainpage.objects.get(main_id = mainpage_id)
        collection(Mainpage)
        Commodity_collection = comm_collection_id
        Commodity_collection_display = []
        Expert_collection = expert_collection_id
        Expert_collection_display = []
        if comm_collection_num > 6:
            Commodity_collection_num = 6
            for i in range(0, 6):
                Commodity_collection_display.append(Commodity_collection[i])
        else:
            Commodity_collection_num = comm_collection_num
            Commodity_collection_display = Commodity_collection
        if expert_collection_num > 6:
            Expert_collection_num = 6
            for i in range(0, 6):
                Expert_collection_display.append(Expert_collection[i])
        else:
            Expert_collection_num = expert_collection_num
            Expert_collection_display = Expert_collection
         #所有报告
        reports = models.Classification.objects.filter(user_user=user)
        print(reports)
        return render(request, 'workshop/frontpage.html', locals())
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "所有字段都必须填写！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(user_email=username)
                if user.user_passwd == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.user_id
                    request.session['user_email'] = user.user_email
                    mainpage_id = user.mainpage_main.main_id
                    Mainpage = models.Mainpage.objects.get(main_id = mainpage_id)
                    collection(Mainpage)
                    Commodity_collection = comm_collection_id
                    Commodity_collection_display = []
                    Expert_collection = expert_collection_id
                    Expert_collection_display = []
                    if comm_collection_num > 6:
                        Commodity_collection_num = 6
                        for i in range(0, 6):
                            Commodity_collection_display.append(Commodity_collection[i])
                    else:
                        Commodity_collection_num = comm_collection_num
                        Commodity_collection_display = Commodity_collection
                    if expert_collection_num > 6:
                        Expert_collection_num = 6
                        for i in range(0, 6):
                            Expert_collection_display.append(Expert_collection[i])
                    else:
                        Expert_collection_num = expert_collection_num
                        Expert_collection_display = Expert_collection
                    return render(request, 'workshop/frontpage.html', locals())
                    message = "密码正确！"
                else:
                    message = "密码不正确！"
            except:
                message = "邮箱不存在！"
        #return render(request, 'login/signin.html', {"message": message})
        return render(request, 'login/signin.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login/signin.html', locals())

def allcomment(request):
    if request.method == "POST":
        UserId = request.POST.get("user_id", "")
        user = models.User.objects.get(user_id = UserId)
        mainpage_id = user.mainpage_main.main_id
        Mainpage = models.Mainpage.objects.get(main_id = mainpage_id)
        collection(Mainpage)
        Commodity_collection = comm_collection_id
        Commodity_collection_display = []
        Expert_collection = expert_collection_id
        Expert_collection_display = []
        Commodity_collection_num = comm_collection_num
        Commodity_collection_display = Commodity_collection
        Expert_collection_num = expert_collection_num
        Expert_collection_display = Expert_collection
    return render(request, 'workshop/all_comments.html', locals())

def allexpert(request):
    if request.method == "POST":
        UserId = request.POST.get("user_id", "")
        user = models.User.objects.get(user_id = UserId)
        mainpage_id = user.mainpage_main.main_id
        Mainpage = models.Mainpage.objects.get(main_id = mainpage_id)
        collection(Mainpage)
        Commodity_collection = comm_collection_id
        Commodity_collection_display = []
        Expert_collection = expert_collection_id
        Expert_collection_display = []
        Commodity_collection_num = comm_collection_num
        Commodity_collection_display = Commodity_collection
        Expert_collection_num = expert_collection_num
        Expert_collection_display = Expert_collection
    return render(request, 'workshop/all_experts.html', locals())

def apply(request):
    if request.session.get('is_login', None):
        if request.method == "POST":
            UserId = request.session['user_id']
            #UserId = request.POST.get("user_id", "")
            user = models.User.objects.get(user_id = UserId)
            user.user_identity = 1
            user.save()
            return redirect('../', locals())