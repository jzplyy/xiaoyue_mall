from django.urls import path
from app01 import converter,views   # 导入应用中的converter
urlpatterns = [
   path('mobile/<mobile:phone_num>/',views.show_mobile)
]
