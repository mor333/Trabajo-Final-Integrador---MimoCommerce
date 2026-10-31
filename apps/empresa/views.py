from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from apps.empresa.models import Empresa

# Create your views here.
class EmpresaListView(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = 'empresa/list.html'
    context_object_name = 'empresas' # Esta es la variable que se usará en el template con {% for empresa in empresas %} para mostrar las empresas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['puede_crear_empresa'] = not Empresa.objects.exists()
        return context

class EmpresaCreateView(LoginRequiredMixin, CreateView):
    model = Empresa
    fields = '__all__'
    template_name = 'empresa/create.html'
    success_url = reverse_lazy('empresa:empresa_list')

    def dispatch(self, request, *args, **kwargs):
        empresa_existente = Empresa.objects.order_by('pk').first()
        if empresa_existente:
            return redirect('empresa:empresa_detail', pk=empresa_existente.pk)
        return super().dispatch(request, *args, **kwargs)

class EmpresaUpdateView(LoginRequiredMixin, UpdateView):
    model = Empresa
    fields = '__all__'
    template_name = 'empresa/update.html'
    success_url = reverse_lazy('empresa:empresa_list')

class EmpresaDeleteView(LoginRequiredMixin, DeleteView):
    model = Empresa
    template_name = 'empresa/delete.html'
    success_url = reverse_lazy('empresa:empresa_list')

    def dispatch(self, request, *args, **kwargs):
        raise PermissionDenied('No está permitido eliminar la empresa registrada.')

class EmpresaDetailView(LoginRequiredMixin, DetailView):
    model = Empresa
    template_name = "empresa/detail.html"
    context_object_name = "empresa" # Nombre de la variable
    # para usar en el template