# -*- encoding: utf-8 -*-
from django.shortcuts import redirect
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

class CobrosView(TemplateView):
    template_name = 'caja/cobros/cobrar/cobros.html'


class CuadrarView(TemplateView):
    template_name = 'caja/cobros/cuadrar/cuadrar.html'


class DevolucionesView(TemplateView):
    template_name = 'caja/cobros/reportes/devoluciones.html'


class FaltantesView(TemplateView):
    template_name = 'caja/cobros/reportes/faltantes.html'
