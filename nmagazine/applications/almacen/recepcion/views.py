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


class MagazineUpdateView(UpdateView):
    model = Magazine
    form_class = MagazineForm
    success_url = '/'
    template_name = 'almacen/recepcion/magazine/update.html'

    def get_initial(self):
        day_ls = MagazineDay.objects.get(
            magazine=self.get_object(),
            day='0',
        )
        day_d = MagazineDay.objects.get(
            magazine=self.get_object(),
            day='1',
        )

        # recuperamos el objeto equipo
        initial = super(MagazineUpdateView, self).get_initial()
        initial['precio_tapa'] = day_ls.precio_tapa
        initial['precio_guia'] = day_ls.precio_guia
        initial['precio_venta'] = day_ls.precio_venta
        initial['precio_tapad'] = day_d.precio_tapa
        initial['precio_guiad'] = day_d.precio_guia
        initial['precio_ventad'] = day_d.precio_venta
        return initial

    def form_valid(self, form):
        #recuperamos los nuevos valores de formulario
        precio_tapa = form.cleaned_data['precio_tapa']
        precio_guia = form.cleaned_data['precio_guia']
        precio_venta = form.cleaned_data['precio_venta']
        precio_tapad = form.cleaned_data['precio_tapad']
        precio_guiad = form.cleaned_data['precio_guiad']
        precio_ventad = form.cleaned_data['precio_ventad']

        #recuperamos DAY Lunes a Sabado
        day_ls = MagazineDay.objects.get(
            magazine=self.get_object(),
            day='0',
        )
        #guardamos los nuevos datos
        day_ls.precio_tapa = precio_tapa
        day_ls.precio_guia = precio_guia
        day_ls.precio_venta = precio_venta
        day_ls.user_modified = self.request.user

        #recuperamos day de domingo
        day_d = MagazineDay.objects.get(
            magazine=self.get_object(),
            day='1',
        )
        #guardamos los nuevos datos
        day_d.precio_tapa = precio_tapad
        day_d.precio_guia = precio_guiad
        day_d.precio_venta = precio_ventad
        day_d.user_modified = self.request.user

        day_ls.save()
        day_d.save()
        return super(MagazineUpdateView, self).form_valid(form)


class MagazineDeleteView(DeleteView):
    model = Magazine
    success_url = '/'
    template_name = template_name = 'almacen/recepcion/magazine/delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.disable = True
        self.object.user_modified = self.request.user
        self.object.save()
        success_url = self.get_success_url()

        return HttpResponseRedirect(success_url)


class MagazineListView(TemplateView):
    template_name = 'almacen/recepcion/magazine/list.html'


class GuideRegisterView(TemplateView):
    template_name = 'almacen/recepcion/guide/add.html'
