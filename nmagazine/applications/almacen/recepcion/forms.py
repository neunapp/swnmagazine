from django import forms

from .models import Magazine, MagazineDay, Guide, DetailGuide

from applications.almacen.entidad.models import Provider

class MagazineForm(forms.ModelForm):
    '''forulario para registrar un producto'''

    precio_tapa = forms.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    precio_guia = forms.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    precio_venta = forms.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    precio_tapad = forms.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    precio_guiad = forms.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    precio_ventad = forms.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    class Meta:
        model = Magazine
        fields = (
            'name',
            'provider',
            'description',
            'day_expiration',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Descripcion',
                }
            ),
            'day_expiration': forms.TextInput(
                attrs={
                    'placeholder': 'Dias de Vencimiento',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(MagazineForm, self).__init__(*args, **kwargs)
        self.fields['provider'].queryset = Provider.objects.filter(
            disable=False,
        )

    def clean_precio_tapa(self):
        precio_tapa = self.cleaned_data['precio_tapa']

        if precio_tapa < 0:
            msj = 'no puede tener un precio menor a cero'
            self.add_error('precio_tapa', msj)
        else:
            return precio_tapa

    def clean_precio_guia(self):
        precio_guia = self.cleaned_data['precio_guia']

        if precio_guia < 0:
            msj = 'no puede tener un precio menor a cero'
            self.add_error('precio_guia', msj)
        else:
            return precio_guia

    def clean_precio_venta(self):
        precio_venta = self.cleaned_data['precio_venta']

        if precio_venta < 0:
            msj = 'no puede tener un precio menor a cero'
            self.add_error('precio_venta', msj)
        else:
            return precio_venta

    def clean_precio_tapad(self):
        precio_tapad = self.cleaned_data['precio_tapad']

        if precio_tapad < 0:
            msj = 'no puede tener un precio menor a cero'
            self.add_error('precio_tapad', msj)
        else:
            return precio_tapad

    def clean_precio_guiad(self):
        precio_guiad = self.cleaned_data['precio_guiad']

        if precio_guiad < 0:
            msj = 'no puede tener un precio menor a cero'
            self.add_error('precio_guiad', msj)
        else:
            return precio_guiad

    def clean_precio_ventad(self):
        precio_ventad = self.cleaned_data['precio_ventad']

        if precio_ventad < 0:
            msj = 'no puede tener un precio menor a cero'
            self.add_error('precio_ventad', msj)
        else:
            return precio_ventad
