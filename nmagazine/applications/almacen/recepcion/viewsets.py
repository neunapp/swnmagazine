from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from datetime import datetime

from applications.almacen.entidad.models import Provider

from .models import Magazine, MagazineDay, Guide, DetailGuide
from .serializers import (
    MagazineDaySerializer,
    GuideSerializer,
    MagazineSerializer,
    GuideListSerializer,
    DetailGuideSerializer,
    DGcreateSerializer,
)
from .functions import guide_detail


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


class GuideListViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.filter(
        anulate=False,
    )
    serializer_class = GuideListSerializer


class GuideViewSet(viewsets.ViewSet):

    def create(self, request):
        serializado = GuideSerializer(data=request.data)
        if serializado.is_valid():
            #recuperamos datos de Guia
            number = serializado.validated_data['number']
            number_invoce = serializado.validated_data['invoce']
            proveedor = serializado.validated_data['provider']
            provider = Provider.objects.get(pk=proveedor)
            date = datetime.now()
            if not Guide.objects.filter(number=number).exists():
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

                res = {'respuesta':'Guardado Correctamente','id':'0'}
            else:
                res = {'respuesta':'ya existe el numero de guia','id':'1'}
        else:
            print serializado.errors
        return Response(res)


class DetailGuideViewSet(viewsets.ModelViewSet):
    serializer_class = DetailGuideSerializer

    def get_queryset(self):
        pk_dg = self.kwargs['pk']
        guide = Guide.objects.get(pk=pk_dg)
        queryset = DetailGuide.objects.filter(
            guide=guide,
            anulate=False,
        )
        return queryset


class DGdeleteViewSet(viewsets.ViewSet):

    def destroy(self, request, *args, **kwargs):
        #recuperamos los datos de url
        pk_guia = self.kwargs['guia']
        #recuperamos el detalle de guia
        print '=====accedio al sistema======'
        print pk_guia
        guide_detail = DetailGuide.objects.get(
            pk=pk_guia,
        )
        print guide_detail
        guide_detail.user_modified = self.request.user
        guide_detail.anulate = True
        #eliminamos la guiadetalle
        guide_detail.save()
        print 'guardado correctamente'

        return Response()


class DGcreateViewSet(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        serializado = DGcreateSerializer(data=request.data)
        if serializado.is_valid():
            #guardamos la nueva guia detalle
            guide = serializado.validated_data['guide']
            #recuperamos guia como objeto
            guide.user_modified=self.request.user
            guide.save()

            magazine_day = serializado.validated_data['magazine_day']
            count = serializado.validated_data['count']

            detail_guide = DetailGuide(
                magazine_day=magazine_day,
                guide=guide,
                count=count,
                precio_unitario=magazine_day.precio_venta,
                precio_tapa=magazine_day.precio_tapa,
                precio_guia=magazine_day.precio_guia,
                precio_sunat=magazine_day.precio_guia,
                user_created=self.request.user,
            )
            detail_guide.save()
        else:
            print serializado.errors

        return Response()
