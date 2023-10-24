from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
from django.contrib.auth.models import AbstractUser
# Create your models here.




class User(AbstractUser):
    first_name=models.CharField(max_length=20,blank=True,null=True)
    last_name=models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField(max_length=255,unique=True)
    password= models.CharField(max_length=200)
    idnumber=models.CharField(max_length=10)
    phone = models.CharField(default="0712345678",null=True,blank=True,max_length=20)
    username = models.CharField(max_length=50, null=True)
    otp=models.CharField(max_length=6,blank=True,null=True)
    # searches=models.ManyToManyField(Recommendations,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
    

    def save(self,*args,**kwargs):
        number_list=[x for x in range(10000,1000000)]
        code_items_for_otp=[]

        for i in range(6):
            num=random.choice(number_list)
            code_items_for_otp.append(num)
        for item in code_items_for_otp:
            code_string = "".join(str(item))

        self.otp=code_string
        super().save(*args,**kwargs)
