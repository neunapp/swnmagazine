from django.conf.urls import url, include
from . import views
from .models import Guide
from rest_framework import routers
from .viewsets import MagazineDayViewSet, GuideViewSet

router = routers.SimpleRouter()
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
        r'^almacen/recepcion/guide/add/$',
        views.GuideRegisterView.as_view(),
        name='guide-add'
    ),
]
