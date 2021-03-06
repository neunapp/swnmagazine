# -*- encoding: utf-8 -*-

from rest_framework import serializers
from .models import Magazine, Guide, MagazineDay, DetailGuide


class CountListField(serializers.ListField):
    child = serializers.IntegerField(
        min_value=1,
        max_value=100000,
    )


class ProdListField(serializers.ListField):
    child = serializers.CharField()


class MagazineSerializer(serializers.ModelSerializer):
    provider = serializers.CharField(source='provider.name')
    tipo = serializers.SerializerMethodField()
    class Meta:
        model = Magazine
        fields = (
            'pk',
            'name',
            'tipo',
            'provider',
            'description',
        )

    def get_tipo(self,obj):
        return obj.get_tipo_display()


class MagazineDaySerializer(serializers.ModelSerializer):
    magazine = serializers.CharField(source='magazine.name')
    day = serializers.SerializerMethodField()
    class Meta:
        model = MagazineDay
        fields = (
            'pk',
            'magazine',
            'day',
        )

    def get_day(self,obj):
        return obj.get_day_display()


class GuideSerializer(serializers.Serializer):
    number = serializers.CharField()
    invoce = serializers.CharField(required=False)
    provider = serializers.CharField()
    counts = CountListField()
    prods = ProdListField()


class GuideListSerializer(serializers.ModelSerializer):
    provider = serializers.CharField(source='provider.name')
    class Meta:
        model = Guide
        fields = (
            'pk',
            'number',
            'date',
            'number_invoce',
            'provider',
            'date_emission',
            'date_retunr_cargo',
            'created',
        )


class DetailGuideSerializer(serializers.ModelSerializer):
    magazine_day = serializers.CharField(source='magazine_day.pk')
    class Meta:
        model = DetailGuide
        fields = (
            'pk',
            'magazine_day',
            'count',
            'guide',
        )


class DGcreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailGuide
        fields = (
            'pk',
            'magazine_day',
            'count',
            'guide',
        )
