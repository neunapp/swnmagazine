# -*- encoding: utf-8 -*-
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from datetime import datetime

from .models import Asignation, DetailAsignation
from .serializers import (
    DetailAsignationSerializer,
    DAsignationSerializer,
    PuataDinamicaSerializer,
    AsignationListSerializer,
    ConsultaSerializer,
)
from .functions import generar_pauta, generar_pauta_dinamica, generar_consulta

from applications.almacen.recepcion.models import DetailGuide
from applications.almacen.entidad.models import Vendor


class DetailAsignationViewSet(viewsets.ModelViewSet):
    serializer_class = DAsignationSerializer

    def get_queryset(self):
        pk_gd = self.kwargs['pk']
        return generar_pauta(pk_gd)


class GenerarPautaDinamica(viewsets.ModelViewSet):
    serializer_class =  PuataDinamicaSerializer

    def get_queryset(self):
        return generar_pauta_dinamica()


class AsignationListViewSet(viewsets.ModelViewSet):
    queryset = Asignation.objects.filter(
        anulate=False,
    )
    serializer_class = AsignationListSerializer


class DACreateViewSet(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        print 'ingreso al detalle'
        #recuperamos el DetalleMagaine
        pk_dm = self.kwargs['pk']
        dmagazine = DetailGuide.objects.get(pk=pk_dm)
        for data in request.data:
            #serializamos la data
            serializado = DAsignationSerializer(data=data)
            if serializado.is_valid():
                #recuperamos canilla
                canilla_id = serializado.validated_data['pk']
                canilla = Vendor.objects.get(pk=canilla_id)
                #verificamos si existe o no una asigancion
                asg, created = Asignation.objects.get_or_create(
                    detail_guide=dmagazine,
                    date=datetime.now(),
                    anulate=False,
                    defaults={
                        'user_created': self.request.user,
                    }
                )

                if not created:
                    #verificamos si ya existe detale asigancion
                    da, cread = DetailAsignation.objects.update_or_create(
                        vendor=canilla,
                        asignation=asg,
                        defaults={
                            'count':serializado.validated_data['count'],
                            'precio_venta':dmagazine.precio_unitario,
                            'user_created':self.request.user,
                        }
                    )
                    #registramos la asignation detalle
                    da.user_modified = self.request.user
                    da.save()
                    print 'se a modificado la asignacion detalle'
                else:
                    asig = Asignation.objects.get(
                        detail_guide=dmagazine,
                        date=datetime.now(),
                        anulate=False,
                    )
                    #registramos la asignacion detalle
                    dasignation = DetailAsignation(
                        vendor=canilla,
                        asignation=asig,
                        count=serializado.validated_data['count'],
                        precio_venta=dmagazine.precio_unitario,
                        user_created=self.request.user,
                    )
                    dasignation.save()
                    print 'se a creado la asinacion detalle'
            else:
                serializado.errors
        return Response()


class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        pk_gd = self.kwargs['pk']
        return generar_consulta(pk_gd)
