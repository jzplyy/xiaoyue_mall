from django.urls import re_path
from . import views
app_name = 'goods'
urlpatterns = [
    # 展示商品数据、添加商品
    re_path(r'^$', views.GoodView.as_view(), name='info'),
    # 修改删除商品
    re_path(r'^goods/(\d*)$', views.UpdateDestoryGood.as_view()),
]
