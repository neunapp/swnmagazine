from django.conf.urls import url, include
from . import views
from .models import Guide
from rest_framework import routers
from .viewsets import MagazineDayViewSet, GuideViewSet, MagazineViewSet

router = routers.SimpleRouter()
router.register(r'magazin', MagazineViewSet)
router.register(r'magazine', MagazineDayViewSet)
router.register(r'save/guide', GuideViewSet, base_name=Guide)

urlpatterns = [
    #url para applications
    url(r'^api/', include(router.urls)),
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
]
