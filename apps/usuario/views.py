from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView

from apps.productos.models import Producto
from apps.servicios.models import Servicio

# Create your views here.
class InicioView(LoginRequiredMixin, TemplateView):
    template_name = 'inicio/inicio.html'

class UsuarioView(TemplateView):
    template_name = 'usuario/usuario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.filter(disponibilidad=True).order_by('nombre')
        context['servicios'] = Servicio.objects.order_by('nombre')
        context['today'] = timezone.localdate()
        return context