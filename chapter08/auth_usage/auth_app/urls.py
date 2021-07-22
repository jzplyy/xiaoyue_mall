from django.urls import path
from . import views
app_name ='auth_app'
urlpatterns = [
    # path('login/', views.LoginView.as_view())
    path('login/', views.LoginView.as_view(),name='login'),
    path('info/',views.user_center,name='info'),
    path('index/',views.IndexView.as_view(),name='index'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
