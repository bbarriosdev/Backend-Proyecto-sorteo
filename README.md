Guía de Configuración y Ejecución del Proyecto
Este proyecto ha sido desarrollado en un entorno Ubuntu. A continuación, se describen los pasos necesarios para configurar el entorno de desarrollo y ejecutar el proyecto de manera correcta.

1. Crear un Entorno Virtual
Primero, necesitamos crear un entorno virtual para aislar las dependencias del proyecto.

-python3 -m venv venv
-source venv/bin/activate


2. Instalar las Dependencias
Con el entorno virtual activado, instala todas las dependencias del proyecto especificadas en el archivo de requerimientos. Este paso descargará e instalará todas las librerías necesarias para ejecutar el proyecto, como Django, Celery y otras dependencias.

-pip install -r requirements.txt


3. Arrancar Celery
Celery se utiliza para ejecutar tareas asíncronas en el proyecto. Para iniciar el worker de Celery, abre una nueva terminal (sin cerrar la que tienes activa para el entorno virtual) y ejecuta el comando correspondiente en la carpeta del proyecto. Esto iniciará el worker de Celery y comenzará a procesar las tareas en segundo plano. Verás logs de las tareas procesadas.

celery -A backend worker --loglevel=info


4. Arrancar el Servidor de Desarrollo de Django
Ahora, vuelve a la terminal donde tienes activado el entorno virtual y ejecuta el comando para arrancar el servidor de desarrollo de Django. Una vez que el servidor esté en funcionamiento, podrás acceder a la aplicación en el navegador en la URL proporcionada por el comando.

python manage.py runserver

Para ingreso al login, se debe usar la ruta 
http://localhost:5173/login 
usuario: bayron
contraseña: 110509
