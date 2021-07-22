from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import reverse


def get_url(request):
    return HttpResponse(f"反向解析的url为：{reverse('url')}")


def login(request):
    return HttpResponse(f"反向解析的url为：{reverse('login')}")


