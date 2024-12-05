# urls.py
from django.urls import path
from .views import GanadorAleatorioView

urlpatterns = [
    path('ganador/', GanadorAleatorioView.as_view(), name='ganador_aleatorio'),
]
