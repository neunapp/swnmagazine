from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from datetime import datetime

from applications.almacen.entidad.models import Provider

from .models import Magazine, MagazineDay, Guide, DetailGuide
from .serializers import MagazineDaySerializer, GuideSerializer, MagazineSerializer


class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.filter(
        disable=False,
    )
    serializer_class = MagazineSerializer


class MagazineDayViewSet(viewsets.ModelViewSet):
    queryset = MagazineDay.objects.filter(
        magazine__disable=False,
    )
    serializer_class = MagazineDaySerializer


class GuideViewSet(viewsets.ViewSet):

    def create(self, request):
        serializado = GuideSerializer(data=request.data)
        if serializado.is_valid():
            #recuperamos datos de Guia
            number = serializado.validated_data['number']
            number_invoce = serializado.validated_data['invoce']
            provider = Provider.objects.get(pk='1')
            date = datetime.now()
            guide = Guide(
                number=number,
                number_invoce=number_invoce,
                provider=provider,
                date=date,
                user_created=self.request.user,
            )
            guide.save()

            #reuperamos datos de MagazinesDay
            counts = serializado.validated_data['counts']
            prods = serializado.validated_data['prods']
            discount = serializado.validated_data['discount']
            afecto = serializado.validated_data['afecto']

            for p,c in zip(prods,counts):
                magazine_day = MagazineDay.objects.get(
                    pk=p,
                )
                guide_detail = DetailGuide(
                    magazine_day=magazine_day,
                    guide=guide,
                    count=c,
                    precio_unitario=magazine_day.precio_venta,
                    precio_tapa=magazine_day.precio_tapa,
                    precio_guia=magazine_day.precio_guia,
                    precio_sunat=magazine_day.precio_guia,
                    dicount=discount,
                    afecto=afecto,
                    user_created=self.request.user,
                )
                guide_detail.save()
        else:
            print serializado.errors
        return Response()
