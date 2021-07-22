from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_mobile(request, phone_num):
    return HttpResponse(f'手机号为：{phone_num}')
