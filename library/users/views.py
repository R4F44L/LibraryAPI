from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializers

# Create your views here.


@api_view(["POST"])
def create_auth(request):
    serialized = serializers.UserSerializer(data=request.data)
    if serialized.is_valid():
        u = serialized.create(serialized.data)
        return Response(u, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer
