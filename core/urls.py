from django.urls import path, re_path
from core import views

app_name = 'core'

urlpatterns = [

    # ------------------------------------- REST -----------------------------------------
    #re_path(r'^test_json/$', views.test_json, name='test_json'),
    path('', views.TestView.as_view(), name='testview'),

    # -------------------------------------------------------------------------------------------------------------------------

    # 이제 여기 저 views.py test_json에 접속하는 주소는 127.0.0.1(기본주소)/r/test_json/ 이 됨.
    # views.py 에서 test_json 을 확인하라.
    # -------------------------------------------------------------------------------------------------------------------------

]
