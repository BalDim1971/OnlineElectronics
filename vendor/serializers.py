from rest_framework import serializers

from products.models import Product
from vendor.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class VendorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        exclude = ('debt',)
