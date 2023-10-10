from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Register_Serializer,User_Serializer,New_Register_Serializer,Book_Serializer
from .models import Register_Model,Book
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
import json
# Create your views here.


class New_Register(APIView):
    def post(self,request):
        data=request.data
        serializer=New_Register_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"ok":serializer.data})
        else:
            return Response({"failed":serializer.errors})
        

class Register(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=User_Serializer(data=data)
           
            if serializer.is_valid():               
                if User.objects.filter(username=serializer.data['username']).exists():
                    return Response({"error":"Username Already Taken"})
                
                # SAVING THE USER dATA
                user=User.objects.create(username=serializer.data['username'])
                user.set_password(raw_password=serializer.data['password'])
                user.save()
                return Response({"data":"Successful","username":str(user.name),"Hash-Password":user.password},status=200)
            
            else:
                return Response({"data":"Failed","errors":serializer.errors},status=401)
        except Exception as e:
            print(e)
            return Response({"error":"Exception Error","data":serializer.errors})

class Login_page(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=User_Serializer(data=data)
            if serializer.is_valid():
                if User.objects.filter(username=request.data['username'],password=request.data['password']).exists():
                    return Response({"Data":"Login Successfully"})
                else:
                    return Response({"Data":"Invalid Username Or Password"})
            else:
                return Response({"Error":serializer.errors})
        except:
            pass


class Home(APIView):
    def get(self,request):
        data=User.objects.all()
        serializer=User_Serializer(data,many=True)
        
        return Response({"payload":serializer.data},status=status.HTTP_200_OK)
    
class Add_Book(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=Book_Serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"payload":serializer.data},status=status.HTTP_200_OK)
            else:
                return Response({"error":serializer.errors})
        except:
            pass

  
class Get_Book(APIView):
    def get(self,request):
        data=Book.objects.all()
        serializer=Book_Serializer(data,many=True)
        
        print(serializer.data)
        return Response({"data":serializer.data})
        
        print("Heri its isss")
        return Response({"data":serializer.errors})