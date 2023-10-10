from rest_framework import serializers
from .models import Register_Model,Book
from django.contrib.auth.models import User
class Register_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Register_Model
        fields=['username',"password","image"]

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password')


class New_Register_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Register_Model
        fields=['username',"password","image"]


class Book_Serializer(serializers.ModelSerializer):
    author=New_Register_Serializer()
    class Meta:
        model=Book
        fields=("title",'author')
        #depth=1
        
        