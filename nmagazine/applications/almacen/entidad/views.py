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
    View,
)

from .models import Provider
from .forms import ProviderForm

# Create your views here.
class ProviderCreateView(CreateView):
    '''registrar un proveedor'''
    form_class = ProviderForm
    success_url = success_url = reverse_lazy('entidad_app:provider-list')
    template_name = 'almacen/entidad/proveedor/add.html'

    def form_valid(self, form):
        provider = form.save(commit=False)
        provider.user_created = self.request.user
        provider.save()

        return super(ProviderCreateView, self).form_valid(form)


class ProviderUpdateView(UpdateView):
    '''modificar proveedor'''
    model = Provider
    form_class = ProviderForm
    success_url = reverse_lazy('entidad_app:provider-list')
    template_name = 'almacen/entidad/proveedor/update.html'

    def form_valid(self, form):
        form.save()
        proveedor = self.get_object()
        proveedor.user_modified = self.request.user
        proveedor.save()

        return super(ProviderUpdateView, self).form_valid(form)


class ProviderDeleteView(DeleteView):
    model = Provider
    success_url = success_url = reverse_lazy('entidad_app:provider-list')
    template_name = 'almacen/entidad/proveedor/delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.disable = True
        self.object.user_modified = self.request.user
        self.object.save()
        success_url = self.get_success_url()

        return HttpResponseRedirect(success_url)


class ProviderListView(ListView):
    context_object_name = 'provider_list'
    template_name = 'almacen/entidad/proveedor/list.html'

    def get_queryset(self):
        return Provider.objects.filter(disable=False)
