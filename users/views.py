from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

#! bu projede third party package (dj-rest-auth) ile login logout işlemlerini yaptık ve token i signal aracılığıyla oluşturduk. 18_Auth_Permission projesindeki auth işlemleri ve token üretimini farklı bir yoldan yapıyordu. Ama o projede de browsable API de login ve logout templateleri yoktu ve bu işlemleri ancak postman üzerinden yapıyoruz. 

#! RegisterView>create içindeki if bloğu 'bu kullanıcıya ait Token varsa token i serializer ın dönen datasına ekle/gönder diyor. Aslında else bloğuna gerek yok/kullanışsız. Çünkü signal ile her üretilen kullanıcı için Token oluşturuyoruz. Buraya eklenmesinin sebebi signal i kapatıp deneme yapmak için 

#! alttaki gibi signalle oluşturup if ile getirmek yerine get_or_create() ile daha kısa sürede oluşuturulabilirmiş.

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data['token'] = "No token created for this user!"
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers) 
        

        