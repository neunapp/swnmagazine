from django.conf.urls import url
from . import views

urlpatterns = [
    url(
    #urls para Proveedor
        r'^almacen/entidad/proveedor/add/$',
        views.ProviderCreateView.as_view(),
        name='provider-add'
    ),
    url(
        r'^almacen/entidad/proveedor/update/(?P<pk>\d+)/$',
        views.ProviderUpdateView.as_view(),
        name='provider-update'
    ),
    url(
        r'^almacen/entidad/proveedor/delete/(?P<pk>\d+)/$',
        views.ProviderDeleteView.as_view(),
        name='provider-delete'
    ),
    url(
        r'^almacen/entidad/proveedor/lista/$',
        views.ProviderListView.as_view(),
        name='provider-list'
    ),
]
