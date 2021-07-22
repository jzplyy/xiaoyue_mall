from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def blog(request, blog_id):
    return HttpResponse(f'参数blog_id值为：{blog_id}')
