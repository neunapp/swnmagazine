# -*- encoding: utf-8 -*-
from rest_framework import serializers

from .models import DetailAsignation, Asignation

from applications.almacen.recepcion.serializers import CountListField, ProdListField

class DetailAsignationSerializer(serializers.ModelSerializer):
    asignation = serializers.CharField(source='asignation.vendor.name')
    class Meta:
        model = DetailAsignation
        fields = (
            'asignation',
            'count',
        )


class DAsignationSerializer(serializers.Serializer):
    pk = serializers.CharField()
    name = serializers.CharField(required=False)
    count = serializers.IntegerField(required=False)
    returned = serializers.IntegerField(required=False)


class ConsultaSerializer(serializers.Serializer):
    pk = serializers.CharField()
    name = serializers.CharField(required=False)
    count = serializers.IntegerField(required=False)
    returned = serializers.IntegerField(required=False)
    total = serializers.IntegerField(required=False)
    total_returned = serializers.IntegerField(required=False)


class PuataDinamicaSerializer(serializers.Serializer):
    pk = serializers.CharField()
    name = serializers.CharField(required=False)
    count = CountListField()
    product = ProdListField()


class AsignationListSerializer(serializers.ModelSerializer):
    detail_guide = serializers.CharField(source='detail_guide.magazine_day.magazine')
    class Meta:
        model = Asignation
        fields = (
            'pk',
            'detail_guide',
            'date',
            'user_created',
        )
