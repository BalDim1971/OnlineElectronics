from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView,
                                     ListAPIView)

from vendor.models import Vendor
from users.permissions import IsActive
from vendor.serializers import (VendorSerializer, VendorUpdateSerializer)


class VendorListApiView(ListAPIView):
    """Чтение списка продавцов"""
    serializer_class = VendorSerializer
    permission_classes = [IsActive]
    queryset = Vendor.objects.all()
    filter_backends = [DjangoFilterBackend]
    search_fields = ['contacts__country',]
    filterset_fields = ['contacts__country',]


class VendorCreateApiView(CreateAPIView):
    """Создаем продавца"""
    serializer_class = VendorSerializer
    permission_classes = [IsActive]


class VendorRetrieveApiView(RetrieveAPIView):
    """Подробности о продавце"""
    serializer_class = VendorSerializer
    permission_classes = [IsActive]
    queryset = Vendor.objects.all()


class VendorUpdateApiView(UpdateAPIView):
    """Обновление данных о продавце"""
    serializer_class = VendorUpdateSerializer
    permission_classes = [IsActive]
    queryset = Vendor.objects.all()


class VendorDestroyApiView(DestroyAPIView):
    """Удаление данных о продавце"""
    serializer_class = VendorSerializer
    permission_classes = [IsActive]
    queryset = Vendor.objects.all()
