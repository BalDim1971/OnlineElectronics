# Generated by Django 5.0.6 on 2024-05-17 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_alter_vendor_debt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendor',
            options={'ordering': ('name',), 'verbose_name': 'объект', 'verbose_name_plural': 'объекты'},
        ),
    ]
