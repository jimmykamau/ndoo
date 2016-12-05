from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework_swagger.views import get_swagger_view

from api.serializers import (
    BucketListSerializer, BucketListItemSerializer, UserRegisterSerializer)
from bucketlist.models import BucketList, BucketListItem


schema_view = get_swagger_view(title='Ndoo API')


@api_view(['GET', 'POST'])
def bucketlist_controls(request):
    """
    Bucketlists
    ---
    parameters:
        - name: body
          ptype: BucketListSerializer
          paramType: body
    """

    if request.method == 'GET':
        bucketlists = BucketList.objects.filter(
            created_by=request.user).all()
        serializer = BucketListSerializer(bucketlists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['created_by'] = request.user.id
        serializer = BucketListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def single_bucketlist_controls(request, id):
    try:
        bucketlist = BucketList.objects.get(pk=id, created_by=request.user)
    except BucketList.DoesNotExist:
        return Response(
            "Bucketlist doesn't exist or user doesn't own it",
            status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        data['created_by'] = request.user.id
        serializer = BucketListSerializer(bucketlist, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bucketlist.delete()
        return Response(
            "Bucketlist deleted successfully",
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def bucketlistitem_controls(request, id):
    try:
        bucketlist = BucketList.objects.get(pk=id, created_by=request.user)
    except BucketList.DoesNotExist:
        return Response(
            "Bucketlist doesn't exist or user doesn't own it",
            status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        bucketlist_items = BucketListItem.objects.filter(
            bucketlist_id=bucketlist).all()
        serializer = BucketListItemSerializer(
            bucketlist_items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['bucketlist_id'] = bucketlist.id
        serializer = BucketListItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def single_bucketlistitem_controls(request, id, item_id):
    try:
        bucketlist = BucketList.objects.get(
            pk=id, created_by=request.user)
        bucketlist_item = BucketListItem.objects.get(
            pk=item_id, bucketlist_id=bucketlist.id)
    except BucketList.DoesNotExist:
        return Response(
            "Bucketlist doesn't exist or user doesn't own it",
            status=status.HTTP_400_BAD_REQUEST)
    except BucketListItem.DoesNotExist:
        return Response(
            "Bucketlist item doesn't exist or user doesn't own it",
            status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        data['bucketlist_id'] = item_id
        serializer = BucketListItemSerializer(bucketlist_item, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bucketlist_item.delete()
        return Response(
            "Bucketlist item deleted successfully",
            status=status.HTTP_204_NO_CONTENT)


class UserRegisterAPIView(generics.CreateAPIView):
    """For /api/v1/auth/register url path"""
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
