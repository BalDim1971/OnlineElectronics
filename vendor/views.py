from django.http import HttpResponseNotFound
from rest_framework.filters import SearchFilter
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView,
                                     ListAPIView)

from vendor.models import Vendor
from users.permissions import IsActive
from vendor.serializers import VendorSerializer, VendorUpdateSerializer


class VendorCreateApiView(CreateAPIView):
    serializer_class = VendorSerializer
    permission_classes = [IsActive]


class VendorRetrieveApiView(RetrieveAPIView):
    serializer_class = VendorSerializer
    permission_classes = [IsActive]
    queryset = Vendor.objects.all()


class VendorUpdateApiView(UpdateAPIView):
    serializer_class = VendorUpdateSerializer
    permission_classes = [IsActive]
    queryset = Vendor.objects.all()


class VendorDestroyApiView(DestroyAPIView):
    serializer_class = VendorSerializer
    permission_classes = [IsActive]
    queryset = Vendor.objects.all()


class VendorListApiView(ListAPIView):
    serializer_class = VendorSerializer
    permission_classes = [IsActive]
    queryset = Vendor.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country',]
    filterset_fields = ['contacts__country',]
