from django.urls import path
from booklist import views


urlpatterns = [

    path('booklist/base/', views.show_base_page),
    path('booklist/detail/', views.show_page),

    path('custom-label/', views.custom_label),
]
