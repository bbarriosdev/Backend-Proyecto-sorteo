
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('registroClient.urls')),
    path('api/usuario/', include('registroUsuario.urls')),
    path('api/sorteo/', include('sorteo.urls')),
]
