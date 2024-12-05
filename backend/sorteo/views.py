# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from registroClient.models import Persona
from registroClient.serializers import PersonaSerializer
import random
from .tasks import send_sorteo_email  

class GanadorAleatorioView(APIView):
    def get(self, request):
        # Filtrar las personas que tienen contraseña
        personas_con_contrasena = Persona.objects.exclude(contrasena__isnull=True).exclude(contrasena="")

        if not personas_con_contrasena:
            return Response({"detail": "No hay personas con contraseña."}, status=404)

        # Elegir un ganador aleatorio
        ganador = random.choice(personas_con_contrasena)

        # Serializar el ganador
        serializer = PersonaSerializer(ganador)

        # Enviar el correo al ganador (enviar correo de la tarea en segundo plano)
        send_sorteo_email.delay(ganador.id)

        return Response({"ganador": serializer.data})
