from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Stock

class StockListView(LoginRequiredMixin, ListView):
    model = Stock
    template_name = 'stock/list.html'
    context_object_name = 'stocks' # Esta es la variable que se usará en el template con {% for stock in stocks %} para mostrar los stocks

class StockCreateView(LoginRequiredMixin, CreateView):
    model = Stock
    fields = '__all__'
    template_name = 'stock/create.html'
    success_url = reverse_lazy('stock:stock_list')

class StockUpdateView(LoginRequiredMixin, UpdateView):
    model = Stock
    fields = '__all__'
    template_name = 'stock/update.html'
    success_url = reverse_lazy('stock:stock_list')

class StockDeleteView(LoginRequiredMixin, DeleteView):
    model = Stock
    template_name = 'stock/delete.html'
    success_url = reverse_lazy('stock:stock_list')

class StockDetailView(LoginRequiredMixin, DetailView):
    model = Stock
    template_name = "stock/detail.html"
    context_object_name = "stock" # Nombre de la variable
    # para usar en el template