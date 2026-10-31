from apps.empresa.models import Empresa


def empresa_encabezado(request):
    return {
        'empresa_encabezado': Empresa.objects.order_by('pk').first(),
    }
