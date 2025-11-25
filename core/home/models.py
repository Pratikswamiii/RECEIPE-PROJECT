from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null=True , blank=True)
    file=models.FileField()

    
class Car(models.Model):
    car_name=models.CharField(max_length=20)
    speed=models.IntegerField(default=50)
