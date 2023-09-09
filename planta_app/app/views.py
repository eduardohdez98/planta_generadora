from django.shortcuts import render
from rest_framework import viewsets, generics, response, views, status
from django.db import models
from django.shortcuts import get_object_or_404
from .models import TipoDispositivo, StatusDispositivo, Dispositivo, Lecturas
from .serializers import (
    TipoDispositivoSerializer,
    StatusDispositivoSerializer,
    DispositivoSerializer,
    LecturasSerializer,
)

# TipoDispositivo Views.


class TipoDispositivoViewSet(viewsets.ModelViewSet):
    queryset = TipoDispositivo.objects.all()
    serializer_class = TipoDispositivoSerializer


# StatusDispositivo Views.


class StatusDispositivoViewSet(viewsets.ModelViewSet):
    queryset = StatusDispositivo.objects.all()
    serializer_class = StatusDispositivoSerializer


# Dispositivo Views


class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer


class DispositivoListView(generics.ListAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer


class DispositivoListByTipoDispositivoView(generics.ListAPIView):
    serializer_class = DispositivoSerializer

    def get_queryset(self):
        id = self.kwargs["id"]
        queryset = Dispositivo.objects.filter(id_tipoDispositivo=id)
        return queryset


class DispositivoDetailView(generics.RetrieveAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer


# Lectura views

class LecturasPost(views.APIView):
    def post(self, request, format=None):
        serializer = LecturasSerializer(data=request.data)
        if serializer.is_valid():
            lecturas = serializer.save()
            
            dispositivo = get_object_or_404(Dispositivo, id=lecturas.id_dispositivo_id)
            dispositivo.potencia_actual = lecturas.potencia_actual
            dispositivo.fecha_actualizacion = lecturas.timestamp
            dispositivo.save()
            
            return status.Response(serializer.data, status=status.HTTP_201_CREATED)
        return status.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LecturasViewSet(viewsets.ModelViewSet):
    queryset = Lecturas.objects.all()
    serializer_class = LecturasSerializer


class LecturasListView(generics.ListAPIView):
    queryset = Lecturas.objects.all()
    serializer_class = LecturasSerializer


class LecturasListByDispositivoView(generics.ListAPIView):
    serializer_class = LecturasSerializer

    def get_queryset(self):
        id = self.kwargs["id"]
        queryset = Lecturas.objects.filter(id_dispositivo=id)
        return queryset


class LecturasListByTipoDispositivoView(generics.ListAPIView):
    serializer_class = LecturasSerializer

    def get_queryset(self):
        id = self.kwargs["id"]
        queryset = Lecturas.objects.filter(id_tipoDispositivo=id)
        return queryset


class LecturaEnergiaTotalByDispositivoView(views.APIView):
    def get(self, request, id):
        lecturas = Lecturas.objects.filter(id_dispositivo=id)
        energia_total = lecturas.aggregate(energia_total=models.Sum("potencia_actual"))[
            "energia_total"
        ]
        return response.Response({"idDispositivo": id, "Energia Total": energia_total})
