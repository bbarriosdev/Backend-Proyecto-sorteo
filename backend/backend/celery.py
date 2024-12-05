# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establecer el nombre del módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Crear una instancia de Celery
app = Celery('backend')

# Usar un backend para las tareas (en este caso, Redis)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Cargar las tareas de Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
