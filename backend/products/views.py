from rest_framework import viewsets
from rest_framework import permissions

from .models import *
from .serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # TODO: Set permissions
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # TODO: Set permissions
    permission_classes = [permissions.AllowAny]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    # TODO: Set permissions
    permission_classes = [permissions.AllowAny]


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    # TODO: Set permissions
    permission_classes = [permissions.AllowAny]


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    # TODO: Set permissions
    permission_classes = [permissions.AllowAny]


__all__ = (
    'CategoryViewSet',
    'ProductViewSet',
    'SupplierViewSet',
    'OfferViewSet',
    'PriceViewSet',
)
