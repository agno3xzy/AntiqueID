from django.shortcuts import render
from . import  models, forms

# Create your views here.
def index(request):
    if request.session.get('is_login', None):
        user_id = request.session['user_id']
        user = models.User.objects.get(user_id = user_id)
        expert = models.Expert.objects.filter()
        return render(request, 'expert/expert_choose.html', locals())
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
                    expert = models.Expert.objects.filter()
                    return render(request, 'expert/expert_choose.html', locals())
                    message = "密码正确！"
                else:
                    message = "密码不正确！"
            except:
                message = "邮箱不存在！"
        return render(request, 'login/signin.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login/signin.html', locals())


class Expert:
    Expert_name = ""
    Expert_avatar = ""
    Expert_comment = ""
    Expert_id = ""
    Time = ""

def comment(request):
    if request.method == "POST":
        commodity_id = request.POST.get("id", '')
        print(commodity_id)
        Commodity = models.Commodity.objects.get(comm_id = commodity_id)
        expert_Commodity = models.ExpertHasCommodity.objects.filter(commodity_comm = commodity_id).reverse()
        EEE = []
        for E in expert_Commodity:
            Expert0 = models.Expert.objects.get(expert_id = E.expert_expert_id)
            EE = Expert()
            EE.Expert_name = Expert0.expert_name
            EE.Expert_avatar = Expert0.expert_avatar
            EE.Expert_comment = E.expert_comment
            EE.Expert_id = E.expert_expert_id
            EE.Time = E.expert_comment_time
            EEE.append(EE)

    return render(request, 'expert/expert_comment.html', locals())

def comment_detail(request):
    if request.method == "POST":
        commodity_id = request.POST.get("comm_id", '')
        expert_id = request.POST.get("expert_id", '')
        print(commodity_id)
        print(expert_id)
        Commodity = models.Commodity.objects.get(comm_id = commodity_id)
        Expert = models.Expert.objects.get(expert_id = expert_id)
        Expert_Comment = models.ExpertHasCommodity.objects.get(commodity_comm = commodity_id, expert_expert = expert_id)

    return render(request, 'expert/expert_comment_detail.html', locals())

class Commodity:
    commodity_id = ""
    commodity_img = ""
    Time = ""
    expert_comment = ""

def detail(request):
    if request.method == "POST":
        expert_id = request.POST.get("expert_id", '')
        Expert = models.Expert.objects.get(expert_id = expert_id)
        Expert_Comment = models.ExpertHasCommodity.objects.filter(expert_expert = expert_id)
        CCC = []
        for C in Expert_Comment:
            Comm = models.Commodity.objects.get(comm_id = C.commodity_comm_id)
            CC = Commodity()
            CC.commodity_id = Comm.comm_id
            CC.commodity_img = Comm.comm_img
            CC.Time = C.expert_comment_time
            CC.expert_comment = C.expert_comment
            CCC.append(CC)

    return render(request, 'expert/expert_detail.html', locals())