from django.urls import path
from .views import StockCreateView, StockDeleteView, StockDetailView, StockListView, StockUpdateView

app_name = "stock"

urlpatterns = [
    path('', StockListView.as_view(), name='stock_list'),
    path('nuevo/', StockCreateView.as_view(), name='stock_create'),
    path('<int:pk>/editar/', StockUpdateView.as_view(), name='stock_update'),
    path('<int:pk>/eliminar/', StockDeleteView.as_view(), name='stock_delete'),
    path('<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
]