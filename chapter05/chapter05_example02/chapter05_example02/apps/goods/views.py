from django.shortcuts import render, redirect, reverse
from django.views import View
from django import http
from .models import Goods


# Create your views here.
class GoodView(View):
    """商品视图类"""

    def get(self, request):
        """展示商品"""
        goods = Goods.objects.all()
        context = {
            'goods': goods,
        }
        return render(request, 'goods.html', context)

    def post(self, request):
        """添加商品"""
        good = Goods()
        try:
            good.name = request.POST.get('good_name')
            good.price = request.POST.get('good_price')
            good.stock = request.POST.get('good_stock')
            good.sales = request.POST.get('good_sales')
            good.save()
            # return redirect('/')  # 快捷方式
            return redirect(reverse('goods:info'))
        except Exception as e:
            return http.HttpResponseForbidden('数据错误')


class UpdateDestoryGood(View):
    """编辑或删除商品"""

    def get(self, request, gid):
        """删除商品数据"""
        try:
            good = Goods.objects.get(id=gid)
            good.delete()
        except Exception as e:
            return http.HttpResponseForbidden('删除失败')
        return redirect(reverse('goods:info'))

    def post(self, request, gid=0):
        """编辑商品"""
        goods = Goods.objects.all()
        count = goods.count()
        try:
            num = request.POST.get('good_num')
            for i in range(1, count + 1):
                if i == int(num):
                    good = goods[i - 1]
                    good.name = request.POST.get('good_name')
                    good.price = request.POST.get('good_price')
                    good.stock = request.POST.get('good_stock')
                    good.sales = request.POST.get('good_sales')
                    good.save()
                    break
        except Exception as e:
            return http.HttpResponseForbidden('编辑失败')
        return redirect(reverse('goods:info'))
