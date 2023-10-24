from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
from django.contrib.auth.models import AbstractUser
from userauth.models import User
# Create your models here.




class Routes(models.Model):
    description=models.CharField(max_length=200)
    start = models.CharField(max_length=100,blank=True,null=True)
    destination = models.CharField(max_length=100,blank=True,null=True)
    fare=models.CharField(max_length=10)
    # sacco=models.ForeignKey(Sacco,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.description
    

class Sacco(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    routes=models.ManyToManyField(Routes,blank=True,)
    # vehicles=models.ManyToManyField(Vehicle,blank=True,)

    def __str__(self) -> str:
        return self.name
    


class Vehicle(models.Model):
    capacity=models.CharField(max_length=5)
    # routes=models.ManyToManyField(Routes,blank=True)
    registration=models.CharField(max_length=100)
    image=models.CharField(max_length=100)
    sacco=models.ForeignKey(Sacco,on_delete=models.CASCADE)


class Seat(models.Model):
    customer=models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING)
    seat_number=models.IntegerField(blank=True,null=True)
    isBooked=models.BooleanField(default=False)



class Trip(models.Model):
    sacco=models.ForeignKey(Sacco,on_delete=models.DO_NOTHING,null=True,blank=True)
    vehicle=models.ForeignKey(Vehicle,on_delete=models.DO_NOTHING,null=True,blank=True)
    routes=models.ForeignKey(Routes,on_delete=models.DO_NOTHING,)
    date=models.DateTimeField(auto_now_add=True)
    pickuppoint=models.CharField(max_length=100,null=True,blank=True)
    seats = models.ManyToManyField(Seat,)



   


# @receiver(pre_save,sender=Trip)
# def addSeats(sender,instance,*args,**kwargs):
#     if instance._state.adding:



# class Trip(models.Model):
#     pass

