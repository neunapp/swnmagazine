from django.conf.urls import url, include
from rest_framework import routers

from . import views, viewsets

from applications.almacen.recepcion.models import DetailGuide

from .models import DetailAsignation
from .viewsets import(
    DetailAsignationViewSet,
    DACreateViewSet,
    GenerarPautaDinamica,
    AsignationListViewSet,
    ConsultaViewSet,
)

router = routers.SimpleRouter()
router.register(r'asignations', AsignationListViewSet)
router.register(
    r'lista/pauta',
    DetailAsignationViewSet,
    base_name=DetailAsignation
)
router.register(
    r'save/asignacion',
    DACreateViewSet,
    base_name=DetailAsignation,
)

urlpatterns = [
    #url para las api de asignacion
    url(r'^api/', include(router.urls)),
    url(
        r'^api/pautas/(?P<pk>[-\w]+)/$',
        viewsets.DetailAsignationViewSet.as_view({'get': 'list'}),
        name='pautas'
    ),
    url(
        r'^api/pautas/dinamica/generar/$',
        viewsets.GenerarPautaDinamica.as_view({'get': 'list'}),
        name='pautas-dinamica'
    ),
    url(
        r'^api/asignacion/save/(?P<pk>[-\w]+)/$',
        viewsets.DACreateViewSet.as_view({'post': 'create'}),
        name='asignacion'
    ),
    url(
        r'^api/asignacion/consulta/(?P<pk>[-\w]+)/$',
        viewsets.ConsultaViewSet.as_view({'get': 'list'}),
        name='entrega-consulta'
    ),
    #url para vistas de asigancion
    url(
        r'^reception/almacen/entregas/list/(?P<pk>\d+)/$',
        views.MagazineDeliverListView.as_view(),
        name='entrega-list'
    ),
    url(
        r'^almacen/recepcion/entrega/registro/(?P<key>\d+)/(?P<pk>\d+)/$',
        views.DetailGuideDetailView.as_view(),
        name='entrega-add'
    ),
    url(
        r'^almacen/recepcion/consulta/lista/$',
        views.ListaConsultaView.as_view(),
        name='entrega-list-consulta'
    ),
    url(
        r'^almacen/recepcion/consulta/ver/(?P<pk>\d+)/$',
        views.DetailConsultaView.as_view(),
        name='consulta-view'
    ),
]
