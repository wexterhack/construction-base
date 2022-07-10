from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'prices', PriceViewSet)


urlpatterns = [
    path('', include(router.urls))
]
