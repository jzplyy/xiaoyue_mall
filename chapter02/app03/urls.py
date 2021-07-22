from django.urls import path

from app03 import views

app_name = 'app03'  # 设置app03应用命名空间

urlpatterns = [
    path('url-reverse/', views.get_url, name='url'),
    path('login/', views.login, name='login'),
]
