from django.urls import path, re_path
from . import views
urlpatterns = [
    # 展示商品数据
    re_path(r'^$', views.get_goods),
    # 删除商品
    re_path(r'^delete(\d+)$', views.del_good),

]
