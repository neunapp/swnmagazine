from __future__ import unicode_literals

from model_utils.models import TimeStampedModel

from datetime import datetime

from django.conf import settings
from django.db import models

from applications.almacen.entidad.models import Vendor
from applications.almacen.recepcion.models import MagazineDay

# Create your models here.
class Asignation(TimeStampedModel):
    """salida de Diario"""
    vendor = models.ForeignKey(Vendor)
    date = models.DateField(
        default=datetime.datetime.today
    )
    anulate = models.BooleanField(default=False)
    returned = models.BooleanField(default=False)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="asignation_created",
        #editable=False
    )
    user_modified = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="asignation_modified",
        blank=True,
        null=True,
        editable=False
    )

    def __str__(self):
        return str(vendor)


class DetailAsignation(TimeStampedModel):
    """Detalle de una salida"""
    magazine_day = models.ForeignKey(MagazineDay)
    asignation = models.ForeignKey(Asignation)
    count = models.PositiveIntegerField()
    retunr_count = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    precio_venta = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="asignationdetail_created",
        #editable=False
    )
    user_modified = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="asignationdetail_modified",
        blank=True,
        null=True,
        editable=False
    )

    def __str__(self):
        return str(MagazineDay)+'--'+str(asignation)
