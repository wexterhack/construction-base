# Generated by Django 4.0.6 on 2022-07-10 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='domain_name',
            field=models.CharField(db_index=True, help_text='Example: `example.com`', max_length=100, unique=True, verbose_name='domain name'),
        ),
    ]