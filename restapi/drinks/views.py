from turtle import st
from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import Drinkserializer
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework import status

# Create your views here.
@api_view(["GET","POST"])
def drink_list(request):
    ##get all the drinks
    #serialize them
    #return json
    if request.method=="GET":
        drinks=Drink.objects.all()
        serializer=Drinkserializer(drinks,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method=="POST":
        serializer=Drinkserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(["GET"])
def send_file(request,filename):

    img = open(filename, 'rb')

    response = FileResponse(img)

    return response
        

    
