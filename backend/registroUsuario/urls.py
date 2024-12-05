# En registroUsuario/urls.py
from django.urls import path
from .views import AdminTokenObtainPairView

urlpatterns = [
    path('token/', AdminTokenObtainPairView.as_view(), name='admin_token_obtain_pair'),
]
