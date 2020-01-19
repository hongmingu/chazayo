"""chazayo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path(r'^r/', include('core.urls')),
    path('', include('core.urls')),


    # -------------------------------------------------------------------------------------------------------------------------

    # path 건 re_path 건 편한대로 쓰면 됨. 내가 path 보다 re path 를 쓰는 것은 예전 장고 버전에서 쓰던 버릇 때문.
    # 여기서 core.urls 기본주소/r/core.url에 적용된 주소로 사용가능함.
    # core 파일의 urls.py로 고

    # -------------------------------------------------------------------------------------------------------------------------

]
