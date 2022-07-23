from django.db import models

# Create your models here.

class Drink(models.Model):
    name=models.CharField(max_length=200)
    discription=models.CharField(max_length=1000)
    drink=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name+" "+self.discription

class uploadimages(models.Model):
    images=models.ImageField(upload_to="images")
