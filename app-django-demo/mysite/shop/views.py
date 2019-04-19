from django.shortcuts import render, redirect
from . import  models, forms


def index(request):
    commid_list = models.Commodity.objects.filter(comm_startprice = 0).order_by('comm_id').values_list('comm_id')
    commid_query = models.Commodity.objects.filter(comm_startprice = 0).order_by('comm_id').values_list('comm_id').reverse()
    commid_max = 0
    if commid_query != None:
        commid_max = commid_query[0]
    commsrc_list = models.Commodity.objects.filter(comm_startprice = 0).values_list('comm_img').order_by('comm_id')
    commstartprice_list = models.Commodity.objects.filter(comm_startprice = 0).values_list('comm_startprice').order_by('comm_id')
    commsellprice_list = models.Commodity.objects.filter(comm_startprice = 0).values_list('comm_sellprice').order_by('comm_id')
    name_list = models.Commodity.objects.filter(comm_startprice = 0).values_list('comm_name').order_by('comm_id')

    comm_num = models.Commodity.objects.filter(comm_startprice = 0).count()
    comm_list = models.Commodity.objects.filter(comm_startprice = 0).filter(comm_con = 0).order_by('comm_id')

    return render(request, 'shop/shop.html', locals())