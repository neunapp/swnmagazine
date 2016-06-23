from rest_framework import viewsets
from .models import Magazine, Guide
from .serializers import MagazineSerializer


class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
