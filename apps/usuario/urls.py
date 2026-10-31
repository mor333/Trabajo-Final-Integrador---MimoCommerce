from django.urls import path
from apps.usuario.views import UsuarioView

app_name = "usuario"

urlpatterns = [
    path('', UsuarioView.as_view(), name='usuario'),
]