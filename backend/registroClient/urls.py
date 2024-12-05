from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet, CompleteRegistrationView

# Crear el router
router = DefaultRouter()
router.register(r'personas', PersonaViewSet, basename='persona')

# Incluir las rutas generadas por el router
urlpatterns = [
    path('', include(router.urls)),
    path('complete-registration/', CompleteRegistrationView.as_view(), name='complete-registration'),
]
