from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
    TemplateView,
    View,
)
from .models import Magazine, MagazineDay
from .forms import MagazineForm
# Create your views here.


class MagazineCreate(CreateView):
    form_class = MagazineForm
    success_url = '/'
    template_name = 'almacen/recepcion/magazine/add.html'

    def form_valid(self, form):
        #verificamos a que tipo se refiere
        parametro = self.kwargs.get('pk', 0)
        #guardamos magazine y recuperaos objeto
        magazine = form.save(commit=False)
        magazine.user_created = self.request.user

        if parametro == '0':
            magazine.tipo = '0'
            magazine.save()
        else:
            magazine.tipo = '1'
            magazine.save()

        #registramos el producto dia-lunes-sabado
        magazine_dia1 = MagazineDay(
            magazine=magazine,
            day='0',
            precio_tapa=form.cleaned_data['precio_tapa'],
            precio_guia=form.cleaned_data['precio_guia'],
            precio_venta=form.cleaned_data['precio_venta'],
            user_created=self.request.user,
        )
        magazine_dia1.save()
        #registro de producto dia-domingo
        magazine_dia2 = MagazineDay(
            magazine=magazine,
            day='1',
            precio_tapa=form.cleaned_data['precio_tapad'],
            precio_guia=form.cleaned_data['precio_guiad'],
            precio_venta=form.cleaned_data['precio_ventad'],
            user_created=self.request.user,
        )
        magazine_dia2.save()

        return super(MagazineCreate, self).form_valid(form)


class GuideRegisterView(TemplateView):
    template_name = 'almacen/recepcion/guide/add.html'
