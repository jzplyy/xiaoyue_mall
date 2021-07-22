import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission, User, Group, ContentType
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import context, RequestContext, loader, Template
from django.urls import reverse
from django.views import View
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# from auth_usage.settings import BASE_DIR
from auth_usage.settings import BASE_DIR


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST['username']  # 用户名
        password = request.POST['password']  # 密码
        remembered = request.POST.get('remembered')  # 记住用户名
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # 设置状态保持
            with open(os.path.join(BASE_DIR, r'templates\index.html'),
                      'r', encoding='utf-8')as f:
                template_string = f.read()
            t = Template(template_string)
            c = RequestContext(request)
            if remembered != 'on':
                # 没有记住用户：浏览器会话结束就过期
                request.session.set_expiry(0)
            else:
                # 记住用户，设置时间，None默认表示两周过期
                request.session.set_expiry(None)
            return redirect(reverse('auth_app:index'), t.render(c))
        else:
            return render(request, 'login.html', {'account_errmsg': '用户名或密码错误'})


@login_required()
def user_center(request):
    return render(request, 'userinfo.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('auth_app:login'))
