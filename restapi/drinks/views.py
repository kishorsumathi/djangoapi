from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import Drinkserializer

# Create your views here.

def drink_list(request):
    ##get all the drinks
    #serialize them
    #return json
    drinks=Drink.objects.all()
    serializer=Drinkserializer(drinks,many=True)
    return JsonResponse(serializer.data,safe=False)
    
