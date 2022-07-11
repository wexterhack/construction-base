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
            'id',
            'name',
            'website',
            'domain_name',
        )
        read_only_fields = ('id',)


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = (
            'id',
            'name',
            'product',
            'supplier',
            'url',
            'price',
        )
        read_only_fields = ('id', 'price',)


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = (
            'id',
            'offer',
            'date',
            'amount',
        )
        read_only_fields = ('id',)


__all__ = (
    'CategorySerializer',
    'ProductSerializer',
    'SupplierSerializer',
    'OfferSerializer',
    'PriceSerializer',
)
