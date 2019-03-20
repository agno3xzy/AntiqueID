from django.shortcuts import render, redirect
from . import  models, forms

def index(request):
    return render(request, 'auction/auction.html')
def auction(request):
    commid_list = models.Commodity.objects.filter(comm_startprice__gt = 0).order_by('comm_id').values_list('comm_id')
    commid_query = models.Commodity.objects.filter(comm_startprice__gt = 0).order_by('comm_id').values_list('comm_id').reverse()
    commid_max = commid_query[0][0]
    commsrc_list = models.Commodity.objects.filter(comm_startprice__gt = 0).values_list('comm_img').order_by('comm_id')
    commstartprice_list = models.Commodity.objects.filter(comm_startprice__gt = 0).values_list('comm_startprice').order_by('comm_id')
    commsellprice_list = models.Commodity.objects.filter(comm_startprice__gt = 0).values_list('comm_sellprice').order_by('comm_id')
    name_list = models.Commodity.objects.filter(comm_startprice__gt = 0).values_list('comm_name').order_by('comm_id')

    comm_num = models.Commodity.objects.filter(comm_startprice__gt = 0).count()
    comm_list = models.Commodity.objects.filter(comm_startprice__gt = 0).order_by('comm_id')

    '''
    for id in commid_max:
        image_src = models.Commidity.objects.filter(comm_id=id).value('comm_image')
        startprice = models.Commidity.objects.filter(comm_id=id).value('comm_startprice')
        sellprice = models.Commidity.objects.filter(comm_id=id).value('comm_sellprice')
    '''



    return render(request,'auction/auction.html', locals())

def details(request):
    commid_list = models.Commodity.objects.filter(comm_startprice__gt = 0).order_by('comm_id').values_list('comm_id')
    commid_query = models.Commodity.objects.filter(comm_startprice__gt = 0).order_by('comm_id').values_list('comm_id').reverse()
    commid_max = commid_query[0][0]
    commsrc_list = models.Commodity.objects.filter(comm_startprice__gt = 0).values_list('comm_img').order_by('comm_id')
    commstartprice_list = models.Commodity.objects.filter(comm_startprice__gt = 0).values_list('comm_startprice').order_by('comm_id')
    commsellprice_list = models.Commodity.objects.filter(comm_startprice__gt = 0).values_list('comm_sellprice').order_by('comm_id')
    name_list = models.Commodity.objects.filter(comm_startprice__gt = 0).values_list('comm_name').order_by('comm_id')
    message = ""
    userprice = 'wrong'
    if request.method == "POST":
        commodity_id = request.POST.get("id", '')
        price_form = forms.PirceForm(request.POST)
        temp_price = models.Commodity.objects.filter(comm_id = commodity_id).values('comm_sellprice')
        name = models.Commodity.objects.filter(comm_id=commodity_id).values('comm_name')
        name0 = name[0]
        startprice = models.Commodity.objects.filter(comm_id=commodity_id).values('comm_startprice')
        startprice0 = startprice[0]
        sellprice = models.Commodity.objects.filter(comm_id=commodity_id).values('comm_sellprice')
        sellprice0 = sellprice[0]
        src = models.Commodity.objects.filter(comm_id=commodity_id).values('comm_img')
        src0 = src[0]
        now_price = temp_price[0]['comm_sellprice']
        if price_form.is_valid():
            userprice = price_form.cleaned_data['userpirce']
            print(userprice)
            print(now_price)
            if int(userprice) <= now_price:
                message = "报价应高于目前最高报价! "
            else:
                models.Commodity.objects.filter(comm_id=commodity_id).update(comm_sellprice=userprice)
                message = "报价成功!"
            return render(request, 'auction/auction_details.html',locals())
    price_form = forms.PirceForm()
    return render(request, 'auction/auction_details.html',locals())

def auction_details(request):
    commid_list = models.Commodity.objects.filter(comm_startprice__gt = 0).order_by('comm_id').values_list('comm_id')
    commid_query = models.Commodity.objects.filter(comm_startprice__gt = 0).order_by('comm_id').values_list('comm_id').reverse()
    commid_max = commid_query[0][0]
    commsrc_list = models.Commodity.objects.filter(comm_startprice__gt = 0).values_list('comm_img').order_by('comm_id')
    commstartprice_list = models.Commodity.objects.filter(comm_startprice__gt = 0).values_list('comm_startprice').order_by('comm_id')
    commsellprice_list = models.Commodity.objects.filter(comm_startprice__gt = 0).values_list('comm_sellprice').order_by('comm_id')
    name_list = models.Commodity.objects.filter(comm_startprice__gt = 0).values_list('comm_name').order_by('comm_id')

    userprice = 'wrong'
    if request.method == "POST":
        commodity_id = request.POST.get("id", '')
        price_form = forms.PirceForm(request.POST)
        name = models.Commodity.objects.filter(comm_id = commodity_id).values('comm_name')
        name0 = name[0]
        startprice = models.Commodity.objects.filter(comm_id = commodity_id).values('comm_startprice')
        startprice0 = startprice[0]
        sellprice = models.Commodity.objects.filter(comm_id = commodity_id).values('comm_sellprice')
        sellprice0 = sellprice[0]
        src = models.Commodity.objects.filter(comm_id = commodity_id).values('comm_img')
        src0 = src[0]
    price_form = forms.PirceForm()
    return render(request, 'auction/auction_details.html',locals())