from rest_framework import serializers

from products.models import Product
from vendor.models import Vendor


class VendorRetrieveSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Vendor
        fields = '__all__'

    def get_products(self, obj):
        """Получаем список продуктов"""
        products = Product.objects.filter(link=obj)
        products_list = []
        products_dict = {}

        for product in products:
            products_dict["name"] = product.name
            products_dict["model"] = product.model
            products_dict["data"] = product.data
            products_list.append(products_dict)
        return products_list


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class VendorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        exclude = ('debt',)
