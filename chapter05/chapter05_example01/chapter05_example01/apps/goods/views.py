from django.shortcuts import render, loader
from .models import Goods
from django import http


# Create your views here.
def get_goods(request):
    """展示商品"""
    t = loader.get_template('goods.html')
    goods = Goods.objects.all()  # 获取所有商品
    context = {
        'goods': goods,
    }
    response = t.render(context, request)
    return http.HttpResponse(response)


def del_good(request, gid):
    """删除指定商品"""
    good = Goods.objects.get(id=gid)
    good.delete()
    return http.HttpResponseRedirect('/')
