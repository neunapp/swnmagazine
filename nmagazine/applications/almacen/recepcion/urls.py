from django.conf.urls import url
from . import views

urlpatterns = [
    url(
    #urls para magazine
        r'^almacen/recepcion/Diario/add/(?P<pk>\d+)/$',
        views.MagazineCreate.as_view(),
        name='magazine-add'
    ),
]
