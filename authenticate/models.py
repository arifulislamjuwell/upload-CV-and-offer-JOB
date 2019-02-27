from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name =models.CharField(max_length=100,blank=True)
    email=models.EmailField(max_length=200,blank=True)
    versity_id_number= models.CharField(max_length=20, blank=True)
    batch=models.CharField(max_length=10,blank=True)
    mobile_number=models.CharField(max_length=15, blank=True)
    gender=models.CharField(max_length=20,blank=True)
    age=models.CharField(max_length=5,blank=True)
    image= models.ImageField(upload_to='profile/',blank=True)
    working=models.CharField(max_length=200,blank=True)
    skill=models.CharField(max_length=200,blank=True)
    facebook=models.CharField(max_length=200,blank=True)
    github=models.CharField(max_length=300,blank=True)
    linkedin= models.CharField(max_length=200,blank=True)
    page_permission=models.CharField(max_length=5,blank=True)

    #def __str__(self):
     #   return self.name
