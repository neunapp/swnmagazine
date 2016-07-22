from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.LogIn.as_view(),
        name='login'
    ),
    url(
        r'^salir/$',
        views.LogoutView.as_view(),
        name='logout'
    ),
    url(
        r'^panel/$',
        views.AlmacenTemplateView.as_view(),
        name='home-almacen'
    ),
    url(
        r'^panel/caja/$',
        views.CajaTemplateView.as_view(),
        name='home-caja'
    ),
]
