# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Persona

@shared_task
def send_registration_email(persona_id):
    try:

        persona = Persona.objects.get(id=persona_id)
        correo = persona.correo
        token = persona.token 
        reset_link = f'{settings.FRONTEND_URL}/{token}/'

 
        send_mail(
            'Completa tu registro',
            f'Hola {persona.nombre},\n\n'
            f'Para completar tu registro, por favor establece tu contraseña accediendo al siguiente enlace:\n\n'
            f'{reset_link}\n\nGracias por registrarte.',
            settings.DEFAULT_FROM_EMAIL,
            [correo],
            fail_silently=False,
        )
    except Exception as e:
   
        raise Exception(f"Error al enviar el correo: {str(e)}")
