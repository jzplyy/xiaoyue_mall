from django.shortcuts import render

# Create your views here.
from django import http


def index(request):
    return http.HttpResponse('hello world')
