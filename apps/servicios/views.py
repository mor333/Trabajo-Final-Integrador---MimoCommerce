from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from apps.servicios.forms import ServicioForm
from apps.servicios.models import Servicio

# Create your views here.
class ServicioListView(LoginRequiredMixin, ListView):
    model = Servicio
    template_name = 'servicios/list.html'
    context_object_name = 'servicios' # Esta es la variable que se usará en el template con {% for servicio in servicios %} para mostrar los servicios

class ServicioCreateView(LoginRequiredMixin, CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicios/create.html'
    success_url = reverse_lazy('servicios:servicio_list')

class ServicioUpdateView(LoginRequiredMixin, UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicios/update.html'
    success_url = reverse_lazy('servicios:servicio_list')

class ServicioDeleteView(LoginRequiredMixin, DeleteView):
    model = Servicio
    template_name = 'servicios/delete.html'
    success_url = reverse_lazy('servicios:servicio_list')

class ServicioDetailView(LoginRequiredMixin, DetailView):
    model = Servicio
    template_name = "servicios/detail.html"
    context_object_name = "servicio" # Nombre de la variable
    # para usar en el template