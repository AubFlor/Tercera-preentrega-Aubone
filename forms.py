from django import forms
from .models import Categoria, Proveedor, Planta

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = '__all__'
