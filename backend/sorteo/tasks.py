# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from registroClient.models import Persona

@shared_task
def send_sorteo_email(persona_id):
    try:
      
        persona = Persona.objects.get(id=persona_id)
        correo = persona.correo
        nombre = persona.nombre  
        token = persona.token 
        
     
        subject = "¡Felicidades, Has Ganado el Sorteo de San Valentín!"
        message = (
            f"¡Hola {nombre}!\n\n"
            f"¡Enhorabuena! Has sido seleccionado como ganador en nuestro sorteo para dos personas "
            f"con todo pagado para celebrar el Día de San Valentín. 🎉💖\n\n"
            f"Prepárate para una experiencia única con tu acompañante. "
            f"Te contactaremos pronto para darte más detalles y coordinar todo para este día especial.\n\n"
            f"Gracias por participar y sigue disfrutando de nuestras promociones.\n\n"
            f"Con cariño,\n"
            f"El equipo de CTS Turismo"
        )

      
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [correo],
            fail_silently=False,
        )
    except Exception as e:
       
        raise Exception(f"Error al enviar el correo: {str(e)}")
