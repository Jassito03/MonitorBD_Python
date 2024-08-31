# Monitor de Base de Datos con Python
## Objetivo:

El objetivo del proyecto es realizar un monitor para Bases de Datos Oracle, el cual despliegue gráficas para la visualización de la información.

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
DNS = localhost/orcl ; Modificar con la ruta a utilizar
PORT = 1521 ; Modificar sólo si la base de datos se encuentra en otro puerto
ENCODIG = UTF-8 ; Modificar sólo si se desea otro tipo de codificación 
```

### Ingresar al entorno de Python
Para ingresar se debe de ejecutar la siguiente instrucción en una terminal situada en la carpeta raíz del proyecto:

**Windows:**
```powershell
.venv\Scripts\activate
```
**MacOS o Linux:**
```bash
source .venv/bin/activate
```

Esto abrirá el entorno virtual Python el cual incluye las liberías utilizadas.
### Correr el programa
Para correr la aplicación se debe ejecutar la siguiente instrucción:
```bash
python .\app.py
```

En la terminal se desplegará la URL para poder ingresar a la página web.

