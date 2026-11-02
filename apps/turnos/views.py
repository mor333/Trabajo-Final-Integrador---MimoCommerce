from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Turno

class TurnoListView(LoginRequiredMixin, ListView):
    model = Turno
    template_name = 'turnos/list.html'
    context_object_name = 'turnos' # Esta es la variable que se usará en el template con {% for turno in turnos %} para mostrar los turnos

class TurnoCreateView(LoginRequiredMixin, CreateView):
    model = Turno
    fields = ['servicio', 'fecha', 'hora', 'estado', 'observaciones']
    template_name = 'turnos/create.html'
    success_url = reverse_lazy('turnos:turno_list')

    def get_initial(self):
        initial = super().get_initial()
        servicio_id = self.request.GET.get('servicio')
        if servicio_id:
            initial['servicio'] = servicio_id
        return initial

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class TurnoUpdateView(LoginRequiredMixin, UpdateView):
    model = Turno
    fields = '__all__'
    template_name = 'turnos/update.html'
    success_url = reverse_lazy('turnos:turno_list')

class TurnoDeleteView(LoginRequiredMixin, DeleteView):
    model = Turno
    template_name = 'turnos/delete.html'
    success_url = reverse_lazy('turnos:turno_list')

class TurnoDetailView(LoginRequiredMixin, DetailView):
    model = Turno
    template_name = "turnos/detail.html"
    context_object_name = "turno" # Nombre de la variable
    # para usar en el template