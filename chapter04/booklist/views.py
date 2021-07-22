from django.shortcuts import render
from dateutil import tz


# Create your views here.
def custom_label(request):
    context = {
        "format_string": "%b %d %Y %H:%M:%S",
        "timezone": tz.gettz('Asia/Shanghai'),
    }
    return render(request, 'results.html', context)




def show_base_page(request):
    return render(request, 'base.html')


def show_page(request):
    return render(request, 'lists.html')
