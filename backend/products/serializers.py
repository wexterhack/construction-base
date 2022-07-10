from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
        )


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'category',
        )


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            'name',
            'website',
            'domain_name',
        )


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = (
            'name',
            'product',
            'supplier',
            'url',
        )


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = (
            'offer',
            'date',
            'amount',
        )


__all__ = (
    'CategorySerializer',
    'ProductSerializer',
    'SupplierSerializer',
    'OfferSerializer',
    'PriceSerializer',
)
