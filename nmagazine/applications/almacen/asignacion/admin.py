from django.contrib import admin

from .models import Asignation, DetailAsignation


class AsignationAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'detail_guide',
        'date',
        'returned',
    )
    list_filter = ('detail_guide',)


class DetailAsignationAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'vendor',
        'asignation',
        'count',
        'retunr_count',
        'precio_venta',
        'anulate',
    )
    list_filter = ('vendor',)
# Register your models here.

admin.site.register(Asignation, AsignationAdmin)
admin.site.register(DetailAsignation, DetailAsignationAdmin)
