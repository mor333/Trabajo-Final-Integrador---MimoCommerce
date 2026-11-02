from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.dateparse import parse_date, parse_time
from django.views.generic import TemplateView

from apps.productos.models import Producto
from apps.servicios.models import Servicio
from apps.turnos.models import Turno

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
        context.setdefault('selected_service_id', self.request.GET.get('servicio', ''))
        context.setdefault(
            'selected_client_name',
            self.request.GET.get('cliente', self.request.user.get_full_name() if self.request.user.is_authenticated else ''),
        )
        context.setdefault('selected_date', self.request.GET.get('fecha', ''))
        context.setdefault('selected_time', self.request.GET.get('hora', ''))
        context.setdefault('selected_product_ids', self.request.GET.getlist('productos'))
        context['booking_saved'] = self.request.GET.get('guardado') == '1'
        return context

    def post(self, request, *args, **kwargs):
        service_id = request.POST.get('servicio', '')
        nombre_cliente = request.POST.get('nombre_cliente', '').strip()
        try:
            servicio = Servicio.objects.get(pk=service_id)
        except (Servicio.DoesNotExist, ValueError, TypeError):
            servicio = None

        fecha = parse_date(request.POST.get('fecha', ''))
        hora = parse_time(request.POST.get('hora', ''))

        if not nombre_cliente:
            error = 'Escribe el nombre del cliente.'
        elif servicio is None:
            error = 'Selecciona un servicio.'
        elif fecha is None:
            error = 'Selecciona una fecha válida.'
        elif fecha < timezone.localdate():
            error = 'La fecha del turno no puede estar en el pasado.'
        elif hora is None:
            error = 'Selecciona una hora válida.'
        else:
            turno = Turno.objects.create(
                usuario=request.user if request.user.is_authenticated else None,
                nombre_cliente=nombre_cliente,
                servicio=servicio,
                fecha=fecha,
                hora=hora,
                estado='Pendiente',
            )
            return redirect(f"{reverse('usuario:usuario')}?guardado=1&turno={turno.pk}")

        context = self.get_context_data(
            selected_service_id=service_id,
            selected_client_name=nombre_cliente,
            selected_date=request.POST.get('fecha', ''),
            selected_time=request.POST.get('hora', ''),
            selected_product_ids=request.POST.getlist('productos'),
            booking_error=error,
        )
        return self.render_to_response(context)