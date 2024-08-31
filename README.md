# Monitor de Base de Datos con Python
## Objetivo:

El objetivo del proyecto es realizar un monitor para la Base de Datos de Oracle, el cual despliegue gráficas para la visualización de la información de la tasa de HITS, por medio del Buffer Caché.

**Librerías utilizadas:**
  * CX_Oracle
  * Flask
  * Pandas
  * Plotly

## ¿Cómo correr el programa?
### Modificar el archivo de configuración
Se deben modificar las variables correspondientes a la base de datos del archivo *"config.example.ini"*, estos datos deben de ser los propios de la base de datos la cuál se va a monitorear. Una vez se modificaron los campos, se debe renombrar el archivo a *"config.ini"*

```ini
[DATABASE]
USERNAME = username ; Usuario que tenga privilegios de SYSDBA en la base de datos
PASSWORD = password ; Modificar con la contraseña del usuario
URL = localhost ; Modificar con la ruta que tenga la base de datos a utilizar
PORT = 1521 ; Modificar sólo si la base de datos se encuentra en otro puerto
SERVICE_NAME = orcl ; Modificar con el nombre del servicio
ENCODIG = UTF-8 ; Modificar sólo si se desea otro tipo de codificación 
```
### Herramientas necesarias
Para saber uso del CX_Oracle se deberá de instalar el build tools de C++. Se podrá instalar según el siguiente enlace: https://visualstudio.microsoft.com/es/visual-cpp-build-tools/

### Ingresar al entorno de Python
Para ingresar se debe de ejecutar la siguiente instrucción en una terminal situada en la carpeta raíz del proyecto:

**Instalación de las librerías**
En el archivo requirements.txt se encuentran todas las liberías y dependencias a instalar, por medio del siguiente comando:
```
pip install -r requirements.txt
```

### Correr el programa
Para correr la aplicación se debe ejecutar la siguiente instrucción:
```bash
python .\app.py
```

En la terminal se desplegará la URL para poder ingresar a la página web.

