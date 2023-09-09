from rest_framework import serializers
from .models import Dispositivo,TipoDispositivo,StatusDispositivo,Lecturas

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'

class TipoDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoDispositivo
        fields='__all__'

class StatusDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model=StatusDispositivo
        fields='__all__'

class LecturasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lecturas
        fields='__all__'