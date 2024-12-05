from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Persona
from .serializers import PersonaSerializer
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tasks import send_registration_email
from rest_framework import serializers

class PersonaViewSet(ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

    def perform_create(self, serializer):
        correo = serializer.validated_data.get('correo')

        # Verificar si el correo ya existe
        if Persona.objects.filter(correo=correo).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")

        # Crear la persona
        persona = serializer.save()

        # Llamar a la tarea asíncrona para enviar el correo
        send_registration_email.delay(persona.id)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from .models import Persona

class CompleteRegistrationView(APIView):
    def post(self, request):
        token = request.data.get('token')
        password = request.data.get('password')
        print("token", token)
        print("password", password)

        if not token or not password:
            raise ValidationError("Faltan datos requeridos.")
        
        # Obtener la persona por el token
        persona = get_object_or_404(Persona, token=token)

        # Verificar si la persona ya tiene contraseña
        if persona.contrasena:
            return Response({"detail": "El cliente ya está registrado."}, status=status.HTTP_400_BAD_REQUEST)

        # Si no tiene contraseña, asignar la nueva
        persona.contrasena = password
        persona.save()

        return Response({"detail": "Registro completado exitosamente."})

    

    
