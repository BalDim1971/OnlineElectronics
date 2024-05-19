from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView,
                                     ListAPIView)

from products.models import Product
from users.permissions import IsActive
from products.serializers import ProductSerializer


class ProductListApiView(ListAPIView):
    """Чтение списка продуктов"""
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('name',)


class ProductCreateApiView(CreateAPIView):
    """Создание данных о продукте"""
    serializer_class = ProductSerializer
    permission_classes = [IsActive]


class ProductRetrieveApiView(RetrieveAPIView):
    """Подробные данные о продукте"""
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
    queryset = Product.objects.all()


class ProductUpdateApiView(UpdateAPIView):
    """Обновление данных о продукте"""
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
    queryset = Product.objects.all()


class ProductDestroyApiView(DestroyAPIView):
    """Удаление данных о продукте"""
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
    queryset = Product.objects.all()
