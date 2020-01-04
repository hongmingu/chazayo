from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class TestView(APIView):
    def get(self, request, *arg, **kwarg):
        request_list = list()

        data1 = {
            'name' : '이희자', 'gender' : '여성', 'interests' : '독서'
        }
        data2 = {
            'name' : '김희자', 'gender' : '여성', 'interests' : '등산'
        }
        data3 = {
            'name' : '이희주', 'gender' : '여성', 'interests' : '요리'
        }
        data4 = {
            'name' : '지화자', 'gender' : '남성', 'interests' : '드라이브'
        }
        data5 = {
            'name' : '이희수', 'gender' : '여성', 'interests' : '수영'
        }

        for i in range(1,6):
            request_list.append(locals()['data'+str(i)])

        return Response(request_list)