from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from apps.productos.forms import ProductoForm
from apps.productos.models import Producto

# Create your views here.
class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'productos/list.html'
    context_object_name = 'productos'

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/create.html'
    success_url = reverse_lazy('productos:producto_list')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/update.html'
    success_url = reverse_lazy('productos:producto_list')

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'productos/delete.html'
    success_url = reverse_lazy('productos:producto_list')

class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = "productos/detail.html"
    context_object_name = "producto" # Nombre de la variable
    # para usar en el template