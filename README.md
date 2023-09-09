# planta_generadora
Microservicio para monitorear una planta generadora

### Requerimientos funcionales:
-Implementar API rest de la solución, preferentemente en Django
- Utilizar base de Datos de SQlite

-implementar CRUD de dispositivos, CRUD de bitácora (tabla de registros)
-Se requieren consultas para:
1) Obtener todos los dispositivos existentes
2) Obtener dispositivos por id
3) Obtener todos los dispositivos por “tipodispositivoId”
4) obtener todas las lecturas guardadas en la bitácora
5) obtener todas las lecturas por id de dispositivos
6) Obtener todas las lecturas por tipo de dispositivo
7) Obtener la energía total (KWh) por cada dispositivo NOTA: para este inciso, por temas 
de examen, considere únicamente sumar las potencias registradas en cada tiempo, 
siempre y cuando sea el mismo id de dispositivo

## Comenzando

Estas instrucciones te ayudarán a configurar y ejecutar el proyecto en tu máquina local.

### Prerrequisitos

- Python 3.x
- Django
- Entorno virtual (opcional pero recomendado)

### Instalación

1. Clona este repositorio:

   
   git clone https://github.com/eduardohdez98/planta_generadora.git
   
Crea un entorno virtual (opcional pero recomendado):


python -m venv venv
source venv/bin/activate  


Instala las dependencias del proyecto:


pip install -r requirements.txt

Aplica las migraciones:


python manage.py migrate


### Uso

Inicia el servidor de desarrollo:


python manage.py runserver
Accede al proyecto en tu navegador web en http://localhost:8000/.
