from rest_framework import serializers
from .models import Magazine, Guide, MagazineDay


class CountListField(serializers.ListField):
    child = serializers.IntegerField(
        min_value=1,
        max_value=100000,
    )


class ProdListField(serializers.ListField):
    child = serializers.CharField()


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
    discount = serializers.DecimalField(
        max_digits=7,
        decimal_places=3,
        required=False,
    )
    afecto = serializers.BooleanField()
