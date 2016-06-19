from __future__ import unicode_literals

from model_utils.models import TimeStampedModel

from datetime import datetime

from django.conf import settings
from django.db import models

from applications.almacen.entidad.models import Provider

# Create your models here.
class Magazine(TimeStampedModel):
    """tabla para magazine y proucto"""
    MAGAZINE_CHOISES = (
        ('0','Diario'),
        ('1','Producto'),
    )
    name = models.CharField(
        max_length=100
    )
    tipo = models.CharField(
        max_length=2,
        choices=MAGAZINE_CHOISES
    )
    provider = models.ForeignKey(Provider)
    description = models.CharField(
        blank=True,
        max_length=100
    )
    day_expiration = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    disable = models.BooleanField(default=False)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="magazine_created",
        #editable=False
    )
    user_modified = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="magazine_modified",
        blank=True,
        null=True,
        editable=False
    )

    def __unicode__(self):
        return self.name


class MagazineDay(TimeStampedModel):
    """Producto Dia"""
    DAY_CHOICES = (
        ('0','Lunes a Sabado'),
        ('1','Domingos'),
    )

    magazine = models.ForeignKey(Magazine)
    day = models.CharField(
        max_length=2,
        choices=DAY_CHOICES
    )
    precio_tapa = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    precio_guia = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    precio_venta = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="magazineday_created",
        #editable=False
    )
    user_modified = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="magazineday_modified",
        blank=True,
        null=True,
        editable=False
    )

    def __str__(self):
        return str(self.magazine)+'-'+self.day


class Guide(TimeStampedModel):
    """Guia de remision"""
    number = models.CharField(
        max_length=20,
    )
    date = models.DateField()
    number_invoce = models.CharField(
        blank=True,
        max_length=100
    )
    date_emission = models.DateField(
        blank=True,
        null=True
    )
    provider = models.ForeignKey(Provider)
    date_retunr_cargo = models.DateField(
        blank=True,
        null=True
    )
    anulate = models.BooleanField(default=True)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="guide_created",
        #editable=False
    )
    user_modified = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="guide_modified",
        blank=True,
        null=True,
        editable=False
    )

    def __str__(self):
        return self.number+'--'+str(self.date)


class DetailGuide(TimeStampedModel):
    """guia detalle"""
    magazine_day = models.ForeignKey(MagazineDay)
    guide = models.ForeignKey(Guide)
    count = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    precio_tapa = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    precio_guia = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    precio_sunat = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    dicount = models.DecimalField(
        max_digits=10,
        decimal_places=3
    )
    missing = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    real_count = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    afecto = models.BooleanField(default=False)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="detailguide_created",
        #editable=False
    )
    user_modified = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="detailguide_modified",
        blank=True,
        null=True,
        editable=False
    )

    def __str__(self):
        return str(self.magazine_day)+'--'+str(self.guide)
