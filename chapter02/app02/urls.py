from django.urls import path, re_path
from app02 import views

urlpatterns = [
    path('blog-list/', views.blog, {'blog_id': 3}),
]
