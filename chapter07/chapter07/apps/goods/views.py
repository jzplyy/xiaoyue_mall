from django.shortcuts import render, redirect, reverse
from django.views import View
from django import http
from .models import Goods
from .forms import GoodForm


# Create your views here.
class GoodView(View):
    """商品视图类"""

    def get(self, request):
        """展示商品"""
        goods = Goods.objects.all()
        form = GoodForm()
        context = {
            'goods': goods,
            'form': form,
        }
        return render(request, 'goods.html', context)

    def post(self, request):
        """添加商品"""
        good = Goods()
        # 使用已提交的数据实例化NameForm
        form = GoodForm(request.POST)
        # 判断表单是否已验证，获取已验证的数据
        if form.is_valid():
            good_data = form.cleaned_data
            good.name = good_data['name']
            good.price = good_data['price']
            good.stock = good_data['stock']
            good.sales = good_data['sales']
            try:
                good.save()
            except:
                return http.HttpResponseForbidden('数据错误')
        return redirect(reverse('goods:info'))


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
        form = GoodForm(request.POST)
        good_num = request.POST.get('good_num')
        if form.is_valid():
            good_data = form.cleaned_data
            for i in range(1, count + 1):
                if i == int(good_num):
                    good = goods[i - 1]
                    good.name = good_data['name']
                    good.price = good_data['price']
                    good.stock = good_data['stock']
                    good.sales = good_data['sales']
                    try:
                        good.save()
                        break
                    except Exception as e:
                        return http.HttpResponseForbidden('编辑失败')
        return redirect(reverse('goods:info'))
