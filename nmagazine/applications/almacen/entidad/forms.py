from django import forms

from .models import Provider, Vendor

#creamos los formularios

class ProviderForm(forms.ModelForm):

    class Meta:
        model = Provider
        fields = (
            'ruc',
            'name',
            'phone',
            'email',
        )

        widgets = {
            'ruc': forms.TextInput(
                attrs={
                    'class': 'form-control input-sm',
                    'placeholder': 'Ingrese el ruc del proveedor'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control input-sm',
                    'placeholder': 'Ingrese el nombre para el proveedor'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control input-sm',
                    'placeholder': 'Ingrese telefono o celular'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control input-sm',
                    'placeholder': 'Ingrese email de proveedor'
                }
            ),
        }

    def clean_ruc(self):
        ruc = self.cleaned_data['ruc']
        if not ruc.isdigit():
            raise forms.ValidationError("Ingrese solo numeros por favor")
        elif len(ruc) < 11:
            raise forms.ValidationError("El ruc debe 11 digitos")
        return ruc

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 4:
            raise forms.ValidationError("nombre demasiado corto")
        return name
