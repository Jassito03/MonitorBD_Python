# Universidad Nacional de Costa Rica
# Monitor para una Base de Datos en Oracle
**Curso:** EIF-402: Administración de Base de Datos

**Profesor:** Msc. Johnny Villalobos Murillo

**Autores**
1. Joseph Piñar Baltodano
2. Abigail Salas Ramírez
3. Gianpablo Moreno Castro

### Objetivo:

Este proyecto tiene como objetivo desarrollar un sistema de monitoreo para la base de datos de Oracle, que permita monitorear el rendimiento y la gestión de recuros con respecto la tasa de Hits en el Buffer Caché (en el SGA), tablespaces y bitácoras.
Se implementan 3 tipos de monitoreo para cada uno de los componentes, donde se podrá visualizar la siguiente información:

**Memoria:** El buffer caché del SGA es donde se almacenan temporalmente los bloques de datos leídos desde disco. La tasa de hits mide la proporción de lecturas que se realizan desde el caché en lugar de desde el disco.
- Lecturas lógicas: Son las lecturas que se satisfacen desde el buffer caché.
- Lecturas físicas: Son las lecturas que requieren acceso al disco. 

Una alta tasa de hits indica un buen uso del caché, mejorando el rendimiento. Mientras que una baja tasa es indicador de que se están realizan una mayor cantidad de lecturas físcas.
Si la tasa de lecturas físicas es alta, puede ser una señal de que el caché está mal configurado o subdimensionado.

**Estructura Física:** Monitorear los tablespaces es crucial para asegurar que haya suficiente espacio disponible para almacenar datos y evitar interrupciones en el funcionamiento de la base de datos. Un tablespace lleno puede causar errores, lo que impacta en la integridad y disponibilidad de los datos. Además, la distribución y el uso de los datos en los tablespaces puede afectar el rendimiento.


**Bitacoras:** Los redo log files son vitales para la recuperación de la base de datos, ya que registran todos los cambios realizados en los datos. Monitorear su estado es importante para:
- Current: Es el redo log file activo, donde se registran los cambios en tiempo real.
- Inactive: Son redo logs que ya han sido archivados o que están listos para ser sobrescritos. Un tamaño o configuración inadecuada de los redo logs puede provocar sobreescrituras frecuentes o tiempos de espera largos, afectando el rendimiento y la capacidad de recuperación en caso de fallo.


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
