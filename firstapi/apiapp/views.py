from django.shortcuts import render
from .models import *
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import EmployeeSerializers
from rest_framework.response import Response
from django.http import HttpResponse, response


@api_view(['POST'])
def create_employee(request):
    s_name = request.GET.get('name')
    s_email = request.GET.get('email')
    s_job = request.GET.get('job')
    x = request.GET.get('search_record')
    if request.method == 'POST':
        a = Employee.objects.filter(name = x)
        if a:
            return Response({"failed": "user name already registered"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serialize_data = EmployeeSerializers(data=request.data)
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({"success": "data created"}, status=status.HTTP_201_CREATED)
            return Response(serialize_data.data, status=status.HTTP_400_BAD_REQUEST)
    return Response({"failed": "POST method"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_allrecord(request):
    if request.method == 'GET':
        moni = Employee.objects.all()
        record = EmployeeSerializers(moni, many=True)
        return Response(record.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_record(request):
    s_record = request.GET.get('search_record', None)
    if request.method == 'PUT':
        try:
            a = Employee.objects.get(name=s_record)
        except Exception as e:
            print(e)
        update = EmployeeSerializers(a, data=request.data)
        if update.is_valid():
            update.save()

            return Response(update.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_record(request):
    record = request.GET.get('search_record', None)
    if request.method == 'DELETE':
        try:
            output = Employee.objects.filter(name=record)
            if output:
                output.delete()
                return Response({"ok": "Record Deleted"}, status=status.HTTP_200_OK)
            else:
                return Response({"failed": "data does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as i:
            print(i)
    return Response({"failed": "failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_filter(request):
    s_record = request.GET.get('search_record', None)
    if request.method == 'GET':
        moni = Employee.objects.filter(name = s_record)
        record = EmployeeSerializers(moni, many=True)
        return Response(record.data, status=status.HTTP_200_OK)
