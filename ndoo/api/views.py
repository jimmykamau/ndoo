from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import UserRegisterSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def bucketlist_controls(request):
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        pass

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def bucketlistitem_controls(request):
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        pass

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass


class UserRegisterAPIView(generics.CreateAPIView):
    """For /api/v1/auth/register url path"""
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
