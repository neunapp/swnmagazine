from django.conf.urls import url, include
from . import views, viewsets
from .models import Guide, DetailGuide
from rest_framework import routers
from .viewsets import (
    MagazineDayViewSet,
    GuideViewSet,
    MagazineViewSet,
    GuideListViewSet,
    DetailGuideViewSet,
    DGdeleteViewSet,
    DGcreateViewSet,
)

router = routers.SimpleRouter()
router.register(r'magazin', MagazineViewSet)
router.register(r'magazine', MagazineDayViewSet)
router.register(r'guides', GuideListViewSet)
router.register(r'save/guide', GuideViewSet, base_name=Guide)
router.register(r'save/detail/guide', DGcreateViewSet, base_name=DetailGuide)

urlpatterns = [
    #url para applications
    url(r'^api/', include(router.urls)),
    url(
        r'^api/update/guide/(?P<pk>[-\w]+)/$',
        viewsets.DetailGuideViewSet.as_view({'get': 'list'}),
        name='guide-items'
    ),
    url(
        r'^api/guide/detail/delete/(?P<guia>[-\w]+)/$',
        viewsets.DGdeleteViewSet.as_view({'post': 'destroy'}),
        name='guide_detail-delete'
    ),
    url(
    #urls para magazine
        r'^almacen/recepcion/Diario/add/(?P<pk>\d+)/$',
        views.MagazineCreate.as_view(),
        name='magazine-add'
    ),
    url(
        r'^almacen/recepcion/Diario/update/(?P<pk>\d+)/$',
        views.MagazineUpdateView.as_view(),
        name='magazine-update'
    ),
    url(
        r'^almacen/recepcion/Diario/delete/(?P<pk>\d+)/$',
        views.MagazineDeleteView.as_view(),
        name='magazine-delete'
    ),
    url(
        r'^almacen/recepcion/Diario/list/$',
        views.MagazineListView.as_view(),
        name='magazine-list'
    ),
    url(
    #urls para diario
        r'^almacen/recepcion/guide/add/$',
        views.GuideRegisterView.as_view(),
        name='guide-add'
    ),
    url(
        r'^almacen/recepcion/guide/list/$',
        views.GuideListView.as_view(),
        name='guide-list'
    ),
    url(
        r'^almacen/recepcion/guide/update/(?P<pk>\d+)/$',
        views.GuideUpdateView.as_view(),
        name='guide-update'
    ),
    url(
        r'^almacen/recepcion/guide/detail/(?P<pk>\d+)/$',
        views.GuideDetailView.as_view(),
        name='guide-detail'
    ),
    url(
        r'^almacen/recepcion/guide/delete/(?P<pk>\d+)/$',
        views.GuideDeleteView.as_view(),
        name='guide-delete'
    ),
    url(
        #urls para guia detalle
        r'^almacen/recepcion/guide/detail/update/(?P<pk>\d+)/$',
        views.DetailGuideUpdateView.as_view(),
        name='detail_guide-update'
    ),
    url(
        r'^almacen/recepcion/guide/detail/delete/(?P<pk>\d+)/$',
        views.DetailGuideDeleteView.as_view(),
        name='detail_guide-delete'
    ),
]
