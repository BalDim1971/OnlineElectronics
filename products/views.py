from rest_framework.filters import SearchFilter
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView,
                                     ListAPIView)

from products.models import Product
from users.permissions import IsActive
from products.serializers import ProductSerializer


class ProductCreateApiView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsActive]


class ProductRetrieveApiView(RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
    queryset = Product.objects.all()


class ProductUpdateApiView(UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
    queryset = Product.objects.all()


class ProductDestroyApiView(DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
    queryset = Product.objects.all()


class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
    queryset = Product.objects.all()
    filter_backends = [SearchFilter]
