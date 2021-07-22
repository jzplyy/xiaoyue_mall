# forms.py
from django.forms import ModelForm
from .models import Goods


class GoodForm(ModelForm):
    class Meta:
        model = Goods
        fields = ['name', 'price', 'sales', 'stock']
        # fields = {'good_name', 'good_price', 'good_sales', 'good_stock'}
    # good_name = forms.CharField(label='商品')
    # good_price = forms.DecimalField(label='价格')
    # good_stock = forms.IntegerField(label='库存')
    # good_sales = forms.IntegerField(label='销量')
