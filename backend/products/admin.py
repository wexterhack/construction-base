from django.contrib import admin

from .models import *


@admin.register(Offer)
class OfferModelAdmin(admin.ModelAdmin):
    pass

