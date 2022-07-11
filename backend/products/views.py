from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response

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
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
