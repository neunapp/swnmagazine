from django.conf.urls import url, include
from rest_framework import routers
from . import views

from .viewsets import ProviderViewSet

router = routers.SimpleRouter()
router.register(r'provider', ProviderViewSet)

urlpatterns = [
    #url para applications
    url(r'^api/', include(router.urls)),
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
