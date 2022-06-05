from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Polls.models import Comida
from rest_comida.serializers import ComidaSerializer

@csrf_exempt
@api_view(['GET','POST'])
def lista_comida(request):
    if request.method == 'GET':
        listaComida =  Comida.objects.all()
        serializer = ComidaSerializer(listaComida, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = ComidaSerializer(data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_comida(request, id):
    try:
        comida = Comida.objects.get(patente=id)
    except Comida.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        seriaz =  ComidaSerializer(comida)
        return Response(seriaz.data)
    elif request.method == "PUT":
        dataP = JSONParser().parse(request)
        seriaz =  ComidaSerializer(comida, data=dataP)
        if seriaz.is_valid():
            seriaz.save()
            return Response(seriaz.data)
        else:
            return Response(seriaz.errors, status = status.HTTP_400_BAD_REQUEST)            
    elif request.method == "DELETE":
        Comida.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)