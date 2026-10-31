from django.urls import path
from .views import EmpresaDetailView, EmpresaListView, EmpresaCreateView, EmpresaUpdateView, EmpresaDeleteView

app_name = "empresa"

urlpatterns = [
    path('', EmpresaListView.as_view(), name='empresa_list'),
    path('nuevo/', EmpresaCreateView.as_view(), name='empresa_create'),
    path('<int:pk>/editar/', EmpresaUpdateView.as_view(), name='empresa_update'),
    path('<int:pk>/eliminar/', EmpresaDeleteView.as_view(), name='empresa_delete'),
    path('<int:pk>/', EmpresaDetailView.as_view(), name='empresa_detail'),
]