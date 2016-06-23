from rest_framework import serializers
from .models import Magazine, Guide


class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = (
            'name',
            'tipo',
            'provider',
            'description',
        )
