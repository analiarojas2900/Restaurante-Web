from rest_framework import serializers
from Polls.models import Comida

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields = ['idPlato', 'precio', 'nombre', 'caracteristica', 'categoria']

