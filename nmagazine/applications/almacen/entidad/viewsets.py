from rest_framework import viewsets, generics

from .models import Provider, Vendor
from .serializers import ProviderSerializer, VendorSerializer, VendorAllSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.filter(
        disable=False,
    )
    serializer_class = ProviderSerializer


class VendorListViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.filter(
        type_vendor='0',
        disable=False,
    )
    serializer_class = VendorSerializer

class VendorAllListViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.filter(
        disable=False,
    )
    serializer_class = VendorAllSerializer
