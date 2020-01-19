from django.http import JsonResponse
from .models import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from. serializer import *
# -------------------------------------------------------------------------------------------------------------------------
# 아래 주어진 것이 REST framework 없이 내가 만들어 쓰던 jsonresponse 기본 예시임. csrf 절차를 @csrf_exempt로 무시해주고 (권장될방법아님)
# 그 요청이 POST 인지 확인하고 어딘가에서 여기에 요청할 때 request 값에 넣어준 'name'이라는 값을 확인해서 name 이란 변수에 넣은 후에 그 값을 조정하는 것임.
# 그런다음 그 값을 바탕으로 우리가 쓰기 편한 리스트 형태를 만들고 JsonResponse로 보내준다.

# -------------------------------------------------------------------------------------------------------------------------

class TestView(generics.CreateAPIView):
    serializer_class = InfobaseSerializer
    queryset = InfoBase.objects.all()

'''
@csrf_exempt
def test_json(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        result = []

        info_bases = InfoBase.objects.filter(school_base__contains=name).all()
        # 형이 주로 쓰게 될 것. 모델해논 것들에서 원하는 조건값을 구해오는 것. 여러가지 옵션이 있을 것임.

        for item in info_bases:
            result.append(item.user_id)

        # 임의로 리스트값을 만들어서 JsonResponse 로 준다. 이게 불편하면 Serializers 를 써도 무방. Json 값을 안드로이드에서 받아야함.
        # 이걸 테스트하기 위해선 사용하면 편한 예시(이미 알고 있을 수도 있다): advanced REST client (모른다면 사용법 확인하길 추천)
        # 이제 core 의 models.py 확인
        return JsonResponse(result, safe=False)
'''