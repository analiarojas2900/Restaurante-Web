from rest_framework import serializers
from Polls.models import Restaurante

class RestauranteeSerializer(serializers.ModelSerializer):
    class Mets:
        mdel = Restaurante
        fields = ['idPlato', 'precio', 'nombre', 'caracteristica', 'categoria']