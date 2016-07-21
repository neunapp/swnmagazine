# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from model_utils.models import TimeStampedModel

from datetime import datetime

from django.conf import settings
from django.db import models

from applications.almacen.asignacion.models import DetailAsignation


class Payment(TimeStampedModel):
    detail_asignation = models.ForeignKey(DetailAsignation)
    count_payment = models.PositiveIntegerField(default=0)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=3,
    )
    date_payment = models.DateTimeField(
        blank=True,
        null=True,
    )
    anulate = models.BooleanField(default=False)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="payment_created",
        #editable=False
    )
    user_modified = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="payment_modified",
        blank=True,
        null=True,
        editable=False
    )

    def __str__(self):
        return str(self.detail_asignation)
