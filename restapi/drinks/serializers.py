from rest_framework import serializers
from django import forms
forms.ModelForm
from .models import Drink,uploadimages 

class Drinkserializer(serializers.ModelSerializer):
    class Meta:
        model=Drink
        fields= ["id","name","discription","drink"]
        #fields = 'all'
class uploadimageserializer(serializers.ModelSerializer):
    class Meta:
        model=uploadimages
        fields=["images"]