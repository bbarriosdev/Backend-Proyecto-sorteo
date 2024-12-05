from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class AdminTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Buscar al usuario
        user = User.objects.filter(username=username).first()
        
        if user:
            # Verificar si la contraseña es correcta
            if user.check_password(password):
                # Verificar si el usuario es superusuario
                if user.is_superuser:
                    return super().post(request, *args, **kwargs)
                else:
                    return Response(
                        {"detail": "Acceso denegado. Solo el administrador puede iniciar sesión."},
                        status=status.HTTP_403_FORBIDDEN,
                    )
            else:
                return Response(
                    {"detail": "Contraseña incorrecta."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"detail": "Usuario no encontrado."},
                status=status.HTTP_404_NOT_FOUND,
            )
