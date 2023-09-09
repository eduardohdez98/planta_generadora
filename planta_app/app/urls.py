from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TipoDispositivoViewSet,
    StatusDispositivoViewSet,
    DispositivoViewSet,
    LecturasViewSet,
    DispositivoListView,
    DispositivoDetailView,
    LecturaEnergiaTotalByDispositivoView,
    LecturasListByDispositivoView,
    LecturasListByTipoDispositivoView,
    LecturasListView,
    DispositivoListByTipoDispositivoView,
    LecturasPost
)

router = DefaultRouter()
router.register(r"tipo_dispositivo", TipoDispositivoViewSet)
router.register(r"status_dispositivo", StatusDispositivoViewSet)
router.register(r"dispositivo", DispositivoViewSet)
router.register(r"lecturas", LecturasViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/dispositivo/<int:id>/', DispositivoDetailView.as_view(), name='dispositivo-detail'),
    path('api/dispositivo/', DispositivoListView.as_view(), name='dispositivo-list'),
    path('api/dispositivo/tipo/<int:id>/', DispositivoListByTipoDispositivoView.as_view(), name='dispositivo-list-by-tipo'),
    path('api/lecturas/energia_total/<int:id>/', LecturaEnergiaTotalByDispositivoView.as_view(), name='lectura-energia-total-by-dispositivo'),
    path('api/lecturas/', LecturasListView.as_view(), name='lecturas-list'),
    path('api/lecturas/tipo/<int:id>/', LecturasListByTipoDispositivoView.as_view(), name='lecturas-list-by-tipo'),
    path('api/lecturas/<int:id>/', LecturasListByDispositivoView.as_view(), name='lecturas-list-by-dispositivo'),
    path('api/lecturas/agregar/', LecturasPost.as_view(), name='add-lecturas'),
]

#curl -X POST http://127.0.0.1:8000/planta_app/api/tipo_dispositivo/ -H "Content-Type: application/json" -d '{"nombre":"Aerogenerador"}'

#
