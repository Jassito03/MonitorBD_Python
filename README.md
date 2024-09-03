# Universidad Nacional de Costa Rica
# Monitor de tasa de Hits para una Base de Datos en Oracle
**Curso:** EIF-402: Administración de Base de Datos
**Profesor:** Msc. Johnny Villalobos Murillo
**Autores**
1. Joseph Piñar Baltodano
2. Abigail Salas Ramírez
3. Gianpablo Moreno Castro

### Objetivo:

Este proyecto tiene como objetivo desarrollar un sistema de monitoreo para bases de datos Oracle, que permita monitorear el rendimiento y la gestión de recuros del Shared Global Area (SGA), específicamente en el Buffer Caché.
En donde se podrá visualizar la siguiente información:
- Porcentaje de la tasa de HITS
- Total de las lecturas físcas 
- Total de las lecturas lógicas

#### Interpretación de la gráfica
1. Si se obtiene una tasa alta de Hit del Buffer Caché es indicativa de un buen rendimiento, puesto a que la mayoría de datos solicitados ya están en la caché.
2. Si la tasa de hit es baja, es indicativo de un mal rendimiento, debido a que los datos solicitados **NO** se encuentran dentro de la caché, por lo que se debe de hacer más las lecturas físicas (en disco), también es posible que se necesite aumentar el tamaño del Buffer Caché. 

### Tecnologías utilizadas

**Lenguajes:**
- Python
- JavaScript
- HTML
  
**Librerías:**
- CX_Oracle
- Flask
- Pandas
- Plotly

### Configuración
#### Modificar el archivo de configuración
Se deben modificar las variables correspondientes a la base de datos del archivo *"config.example.ini"*, estos datos deben de ser los propios de la base de datos la cuál se va a monitorear. Una vez se modificaron los campos, se debe renombrar el archivo a *"config.ini"*

```
[DATABASE]
USERNAME = username ; Usuario que tenga privilegios de SYSDBA en la base de datos
PASSWORD = password ; Modificar con la contraseña del usuario
URL = localhost ; Modificar con la ruta que tenga la base de datos a utilizar
PORT = 1521 ; Modificar sólo si la base de datos se encuentra en otro puerto
SERVICE_NAME = orcl ; Modificar con el nombre del servicio
ENCODING = UTF-8 ; Modificar sólo si se desea otro tipo de codificación 
INSTANCE_CLIENT = ruta; Modificar la ruta en donde se encuentra la instancia del cliente de Oracle
```

## Herramientas necesarias
#### C++ Build Tools
Para saber uso del CX_Oracle se deberá de instalar el build tools de C++. Se podrá instalar según el siguiente enlace: https://visualstudio.microsoft.com/es/visual-cpp-build-tools/

#### Oracle Instance Client
Es necesario haber instalado el Oracle Instance Client para poder establecer la conexión con el sistema, además de haberlo agregado como variable de entorno del sistema.
Para poder descargarlo puede descargarlo en la pagina oficial de Oracle: https://www.oracle.com/database/technologies/instant-client/downloads.html


#### Instalación de las librerías
En el archivo requirements.txt se encuentran todas las liberías y dependencias a instalar. Para poder instalarlas, es necesario dirigirse a la carpeta principal del proyecto **(MonitorBD_Python)**, abrir una terminal en dicho directorio y ejecutar el siguiente comando:
```
pip install -r requirements.txt
```

## Ejecución del programa
Una vez que tenga las herramientas y dependencias instaladas puede proceder a iniciar el servidor, por medio de una terminal en el directorio de **MonitorBD_Python** se deberá de ejecutar la siguiente instrucción:
```bash
python app.py
```
A continuación proceda abrir un naveador y dirígase a **localhost:5000**. Ahí podrá observar un gráfico, en donde en el eje 'Y' se podrá ver el porcentaje y en el 'X'  serán los segundos transcurridos. Los datos mostrados se actualizarán de manera automática cada 5 segundos