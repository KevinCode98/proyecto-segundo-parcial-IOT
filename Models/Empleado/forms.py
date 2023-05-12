from django import forms
from Models.Empleado.models import Empleado

class Formulario(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})}

