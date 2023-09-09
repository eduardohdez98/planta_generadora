from django.db import models

# Create your models here.


class TipoDispositivo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        app_label = 'app'


class StatusDispositivo(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        app_label = 'app'


class Dispositivo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_tipoDipositivo = models.ForeignKey(TipoDispositivo, on_delete=models.CASCADE)
    fecha_alta = models.DateField()
    fecha_actualizacion = models.DateField()
    potencia_actual = models.IntegerField()
    id_statusDispositivo = models.ForeignKey(
        StatusDispositivo, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        app_label = 'app'


class Lecturas(models.Model):
    id = models.AutoField(primary_key=True)
    id_dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    id_tipoDispositivo = models.ForeignKey(TipoDispositivo, on_delete=models.CASCADE)
    potencia_actual = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        app_label = 'app'
