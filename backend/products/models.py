from decimal import Decimal

from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=400,
        blank=False,
        null=False,
        db_index=True,
        verbose_name='name',
        help_text='',
    )


class Product(models.Model):
    name = models.CharField(
        max_length=400,
        blank=False,
        null=False,
        db_index=True,
        verbose_name='name',
        help_text=''
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        verbose_name='category',
        help_text='',
    )


class Supplier(models.Model):
    name = models.CharField(
        max_length=300,
        blank=False,
        null=False,
        db_index=True,
        verbose_name='name',
        help_text='',
    )
    website = models.URLField(
        max_length=400,
        blank=False,
        null=False,
        db_index=False,
        verbose_name='website',
        help_text=''
    )
    domain_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        db_index=True,
        verbose_name='domain name',
        help_text='Example: `example.com`',
        unique=True,
    )


class Offer(models.Model):
    name = models.CharField(
        max_length=300,
        blank=False,
        verbose_name='name',
        db_index=True,
        help_text=''
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.SET_NULL,
        related_name='offers',
        verbose_name='products',
        null=True,
        blank=True,
        default=None,
        help_text='',
    )
    supplier = models.ForeignKey(
        to=Supplier,
        on_delete=models.CASCADE,
        related_name='offers',
        verbose_name='supplier',
        help_text=''
    )
    url = models.URLField(
        blank=False,
        null=False,
        unique=True,
        verbose_name='URL',
        help_text='',
    )

    @property
    def price(self):
        price_obj = self.prices.first()
        return price_obj.amount

    class Meta:
        unique_together = ('product', 'supplier')


class Price(models.Model):
    offer = models.ForeignKey(
        to=Offer,
        on_delete=models.CASCADE,
        related_name='prices',
        blank=False,
        null=False,
        verbose_name='offer',
        help_text=''
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='date',
        blank=True,
        null=False,
    )
    amount = models.DecimalField(
        max_digits=22,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name='amount',
        help_text='Price amount',
    )

    class Meta:
        ordering = ('-date',)


__all__ = (
    'Category',
    'Product',
    'Supplier',
    'Offer',
    'Price',
)
