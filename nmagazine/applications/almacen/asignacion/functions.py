from applications.almacen.recepcion.models import DetailGuide
from applications.almacen.entidad.models import Vendor
from .models import DetailAsignation, Asignation


#creamos calse que rpresenta una pauta

class Pauta():
    pk = ''
    name = ''
    count = 0
    returned = 0


class Consulta():
    pk = ''
    name = ''
    count = 0
    returned = 0
    total = 0
    total_returned = 0


class PautaMultiple():
    pk = ''
    name = ''
    count = []
    product = []


#funcion qeu devuelve lista de pautas de entrega
def generar_pauta(pk):
    #recuperamos el producto dia
    pd = DetailGuide.objects.get(pk=pk).magazine_day
    #recuperamos la lista de canillas
    canillas = Vendor.objects.filter(
        disable=False,
        anulate=False,
    )
    resultado = []
    #generamos lista resultado
    for c in canillas:
        consulta = DetailAsignation.objects.filter(
            vendor=c,
            asignation__detail_guide__magazine_day=pd,
            anulate=False,
        ).order_by('created')
        if consulta:
            #creamos la pautas
            pauta = Pauta()
            pauta.pk = c.pk
            pauta.name = c.name
            pauta.count = consulta[0].count
            peso = 0
            resultado.append(pauta)
        else:
            #creamos la pautas
            pauta = Pauta()
            pauta.pk = c.pk
            pauta.name = c.name
            pauta.count = 0
            resultado.append(pauta)

    return resultado



def generar_consulta(pk):
    #recuperamso la asigancion
    asig = Asignation.objects.get(pk=pk)
    #recuperamos la lista de canillas
    canillas = Vendor.objects.filter(
        disable=False,
        anulate=False,
    )
    resultado = []
    sum_total = 0
    sum_returned = 0
    #generamos lista resultado
    for c in canillas:
        dasig = DetailAsignation.objects.get(
            vendor=c,
            asignation=asig,
            anulate=False,
        )
        if dasig:
            #creamos la pautas
            consulta = Consulta()
            consulta.pk = c.pk
            consulta.name = c.name
            consulta.count = dasig.count
            consulta.returned = dasig.retunr_count
            sum_total = sum_total + dasig.count
            sum_returned = sum_returned + dasig.retunr_count

            resultado.append(consulta)
        else:
            print 'error: no existe la consulta'

    resultado[0].total_returned = sum_returned
    resultado[0].total = sum_total
    return resultado



def generar_pauta_dinamica():
    # recuepramos lista de canillas
    canillas = Vendor.objects.filter(
        anulate=False,
        disable=False,
    )
    #recuperamos la lista de diarios
    lista = DetailGuide.objects.magazine_no_expired()
    # creamos arreglo resultado
    resultado = []
    #iteramos la lista de canillas
    for c in canillas:
        #creamos un ibjeto pauta
        p = PautaMultiple()
        p.pk = c.pk
        p.name = c.name
        p.count =[]
        p.product =[]
        #asignamos cantidad por diario
        for dg in lista:
        #recuperaos ultima asigancion
            consulta = DetailAsignation.objects.filter(
                vendor=c,
                asignation__detail_guide__magazine_day=dg.magazine_day,
                anulate=False,
            ).order_by('created')
            #verificamos si existen datos
            if consulta.exists():
                p.count.append(consulta[0].count)
                p.product.append(consulta[0].asignation.detail_guide.magazine_day)
            else:
                p.count.append(0)
                p.product.append(dg.magazine_day.magazine)

        resultado.append(p)

    return resultado
