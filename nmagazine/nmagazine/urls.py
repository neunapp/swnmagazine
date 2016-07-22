from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib import admin

urlpatterns = [
    url(r'^', include('applications.users.urls', namespace="users_app")),
    url(r'^', include('applications.almacen.entidad.urls', namespace="entidad_app")),
    url(r'^', include('applications.almacen.recepcion.urls', namespace="recepcion_app")),
    url(r'^', include('applications.almacen.asignacion.urls', namespace="asignacion_app")),
    url(r'^', include('applications.caja.pagos.urls', namespace="pagos_app")),

    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
