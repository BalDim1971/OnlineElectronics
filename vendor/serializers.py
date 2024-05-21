from rest_framework import serializers

from contacts.serializers import ContactsSerializer
from products.serializers import ProductSerializer
from vendor.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    """
    Сериализатор для продавцов общий
    """
    products = ProductSerializer(read_only=True, many=True)
    contacts = ContactsSerializer(read_only=True)

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'seller_type', 'level', 'debt', 'date_create',
                  'contacts', 'products', 'vendor']
        # Запрет обновления поля "Задолженность перед поставщиком"
        read_only_fields = ('debt',)


class VendorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        exclude = ('debt',)


class VendorRetrieveSerializer(serializers.ModelSerializer):
    """
    Сериализатор для продавцов подробная информация один уровень
    """
    products = ProductSerializer(read_only=True, many=True)
    contacts = ContactsSerializer(read_only=True)
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'seller_type', 'level', 'debt', 'date_create',
                  'contacts', 'products', 'vendor']
        # Запрет обновления поля "Задолженность перед поставщиком"
        read_only_fields = ('debt',)
