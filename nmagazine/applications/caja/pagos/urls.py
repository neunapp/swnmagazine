from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^caja/cobros/cobrar/cobros$',
        views.CobrosView.as_view(),
        name='pagos-cobrar'
    ),
    url(
        r'^caja/cobros/cuadrar/caja$',
        views.CuadrarView.as_view(),
        name='pagos-cudarar'
    ),
    url(
        r'^caja/cobros/reportes/devolucion$',
        views.DevolucionesView.as_view(),
        name='pagos-devoluciones'
    ),
    url(
        r'^caja/cobros/reportes/deudores$',
        views.FaltantesView.as_view(),
        name='pagos-faltantes'
    ),
]
