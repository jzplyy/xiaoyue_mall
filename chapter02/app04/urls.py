from django.urls import path, include

from app04 import views

# 设置应用命名空间避免出现反向解析URL时出现混淆
app_name = 'app04'  # 设置app04应用命名空间
urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.url_path, name='url_path'),
]
