from django.contrib import admin

from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'detail_asignation',
        'count_payment',
        'amount',
        'date_payment',
        'anulate',
    )
    list_filter = ('detail_asignation',)

# Register your models here.

admin.site.register(Payment)
