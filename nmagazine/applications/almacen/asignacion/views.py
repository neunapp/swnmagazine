from django.shortcuts import render
from datetime import datetime, timedelta
from django.utils import timezone
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

from applications.almacen.recepcion.models import (
    Magazine,
    MagazineDay,
    DetailGuide,
)
from .models import Asignation, DetailAsignation


class MagazineDeliverListView(ListView):
    context_object_name = 'magazin_list'
    template_name = 'almacen/asignacion/entrega/list.html'

    def get_context_data(self, **kwargs):
        context = super(MagazineDeliverListView, self).get_context_data(**kwargs)
        context['key'] = self.kwargs.get('pk',0)
        return context

    def queryset(self):
        queryset = DetailGuide.objects.magazine_no_expired()

        return queryset


class DetailGuideDetailView(DetailView):
    model = DetailGuide
    template_name = 'almacen/asignacion/entrega/add.html'

    def get_context_data(self, **kwargs):
        context = super(DetailGuideDetailView, self).get_context_data(**kwargs)
        context['tipo'] = self.kwargs.get('key',0)
        return context


class ListaConsultaView(TemplateView):
    template_name = 'almacen/asignacion/consulta/list.html'


class DetailConsultaView(DetailView):
    model = Asignation
    template_name = 'almacen/asignacion/consulta/view.html'
