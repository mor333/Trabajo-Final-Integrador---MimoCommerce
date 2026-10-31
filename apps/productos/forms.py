from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'fecha_de_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }
