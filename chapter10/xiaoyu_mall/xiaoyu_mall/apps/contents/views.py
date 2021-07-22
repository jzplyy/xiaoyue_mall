from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request):
        """提供首页广告页面"""
        return render(request, 'index.html')