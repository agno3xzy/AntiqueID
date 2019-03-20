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

    price0 = commstartprice_list[0][0]
    price1 = commstartprice_list[1][0]
    price2 = commstartprice_list[2][0]
    price3 = commstartprice_list[3][0]
    price4 = commstartprice_list[4][0]
    price5 = commstartprice_list[5][0]
    price6 = commstartprice_list[6][0]
    price7 = commstartprice_list[7][0]
    price8 = commstartprice_list[8][0]

    name0 = name_list[0][0]
    name1 = name_list[1][0]
    name2 = name_list[2][0]
    name3 = name_list[3][0]
    name4 = name_list[4][0]
    name5 = name_list[5][0]
    name6 = name_list[6][0]
    name7 = name_list[7][0]
    name8 = name_list[8][0]

    src0 = commsrc_list[0][0]
    src1 = commsrc_list[1][0]
    src2 = commsrc_list[2][0]
    src3 = commsrc_list[3][0]
    src4 = commsrc_list[4][0]
    src5 = commsrc_list[5][0]
    src6 = commsrc_list[6][0]
    src7 = commsrc_list[7][0]
    src8 = commsrc_list[8][0]
    '''
    for id in commid_max:
        image_src = models.Commidity.objects.filter(comm_id=id).value('comm_image')
        startprice = models.Commidity.objects.filter(comm_id=id).value('comm_startprice')
        sellprice = models.Commidity.objects.filter(comm_id=id).value('comm_sellprice')
    '''



    return render(request,'auction/auction.html',locals())

def details(request):
    commid_list = models.Commodity.objects.filter(comm_startprice__gt=0).order_by('comm_id').values_list('comm_id')
    commid_query = models.Commodity.objects.filter(comm_startprice__gt=0).order_by('comm_id').values_list(
        'comm_id').reverse()
    commid_max = commid_query[0][0]
    commsrc_list = models.Commodity.objects.filter(comm_startprice__gt=0).values_list('comm_img').order_by('comm_id')
    commstartprice_list = models.Commodity.objects.filter(comm_startprice__gt=0).values_list(
        'comm_startprice').order_by('comm_id')
    commsellprice_list = models.Commodity.objects.filter(comm_startprice__gt=0).values_list('comm_sellprice').order_by(
        'comm_id')
    name_list = models.Commodity.objects.filter(comm_startprice__gt=0).values_list('comm_name').order_by('comm_id')

    price0 = commstartprice_list[0][0]
    src0 = commsrc_list[0][0]
    name0 = name_list[0][0]
    sellprice0 = commsellprice_list[0][0]

    userprice = 'wrong'
    if request.method == "POST":
        price_form = forms.PirceForm(request.POST)
        temp_price = models.Commodity.objects.filter(comm_id = 0).values('comm_sellprice')
        now_price =str(temp_price[0])
        if price_form.is_valid():
            userprice = price_form.cleaned_data['userpirce']
            if userprice <= now_price :
                message = "报价应高于目前最高报价 "
            else:
                comm_sellprice = userprice
                comm_sellprice.save()
            return render(request, 'auction/auction_details.html',locals())
    price_form = forms.PirceForm()
    return render(request, 'auction/auction_details.html',locals())

