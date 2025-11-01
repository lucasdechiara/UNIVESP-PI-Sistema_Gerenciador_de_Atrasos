#serializer para converter modelos em JSON

from rest_framework import serializers
from .models import RegAtrasos

class RegAtrasosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegAtrasos
        fields = ['id', 'ra', 'data_atraso', 'horario_chegada', 'justificativa']
