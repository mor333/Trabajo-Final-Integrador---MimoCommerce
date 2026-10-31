from django.urls import path
from .views import ServicioCreateView, ServicioDeleteView, ServicioDetailView, ServicioListView, ServicioUpdateView
 
app_name = "servicios"

urlpatterns = [
    path('', ServicioListView.as_view(), name='servicio_list'),
    path('nuevo/', ServicioCreateView.as_view(), name='servicio_create'),
    path('<int:pk>/editar/', ServicioUpdateView.as_view(), name='servicio_update'),
    path('<int:pk>/eliminar/', ServicioDeleteView.as_view(), name='servicio_delete'),
    path('<int:pk>/', ServicioDetailView.as_view(), name='servicio_detail'),
]