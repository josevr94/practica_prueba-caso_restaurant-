from django import forms
from .models import Reserva
from django.core.exceptions import ValidationError
from django.utils import timezone


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente_id','mesa_id','fecha_reserva','estado'] 
        widgets = {
            'fecha_reserva': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        mesa = cleaned_data.get('mesa_id')
        fecha_reserva = cleaned_data.get('fecha_reserva')

        # Verificar si ya existe una reserva para la misma mesa y hora
        if mesa and fecha_reserva:
            # Definir el rango de tiempo que se quiere verificar
            reservas_existentes = Reserva.objects.filter(mesa_id=mesa, fecha_reserva=fecha_reserva)
            if reservas_existentes.exists():
                raise ValidationError("Esta mesa ya está reservada para la fecha y hora seleccionada.")

        return cleaned_data    