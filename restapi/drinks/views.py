from email.mime import image
from turtle import st
import base64 
from django.shortcuts import render,redirect
from email.mime.multipart import MIMEMultipart
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Drink, uploadimages
from .serializers import Drinkserializer,uploadimageserializer
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout

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
        print(request.data)
        serializer=Drinkserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(["GET"])
def send_file(request,filename):

    img = open(filename, 'rb')

    response = FileResponse(img)

    return response
@api_view(["POST","GET"])
def store_data(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]

        user= User.objects.create_user(username=username,password=password,email=email)
        user.save()
        print("user_created")
        return render(request,"auth.html")
    else:
        return render(request,"user.html")
@api_view(["POST","GET"])
def auth(request):

    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
                login(request,user)
                return JsonResponse({"success":True})

        else:
            # No backend authenticated the credentia
                return JsonResponse({"success":False})
    if request.method=="GET":
        return render(request,"auth.html")
    
def logout_user(request):
    logout(request)
    return redirect("/auth")
class UserUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    @api_view(["POST","GET"])
    def button(request):
        if request.method=="GET":
            print("inget")
            return render(request,"collect.html")
        if request.method=="POST":
            #print(request.data)
            serializer=uploadimageserializer(data={"images":request.data["image"],"csrfmiddlewaretoken":request.data["csrfmiddlewaretoken"]})
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

