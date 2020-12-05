from api.serializers import RoomSerializer
from django.shortcuts import render
from rest_framework import  generics
from .models import Room
from .serializers import  RoomSerializer

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    

