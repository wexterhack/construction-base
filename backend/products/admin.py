from django.contrib import admin

from .models import *


@admin.register(Offer)
class OfferModelAdmin(admin.ModelAdmin):
    list_filter = ('supplier',)
    readonly_fields = ('price',)
    list_display = ('name', 'price')

