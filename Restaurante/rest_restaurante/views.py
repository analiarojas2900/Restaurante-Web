from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Polls.models import Restaurante
from rest_restaurante.serializers import RestauranteeSerializer

@csrf_exempt
@api_view(['GET','POST'])

