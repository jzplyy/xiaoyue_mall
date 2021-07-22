from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def login(request):
    return HttpResponse(f"反向解析的url为：{reverse('login')}")


# def url_path(request):
#     return HttpResponse(f"当前url：{reverse('app04:url_path')}")
def url_path(request):
    return HttpResponse(f"当前url:{(reverse('app04:url_path',current_app=request.resolver_match.namespace))}")
