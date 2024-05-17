from django.contrib import admin
from django.urls import path
from vendor.apps import VendorConfig
from vendor.views import (VendorListApiView, VendorCreateApiView, 
                          VendorRetrieveApiView, VendorUpdateApiView,
                          VendorDestroyApiView)

urlpatterns = [
    path('create/', VendorCreateApiView.as_view(),
         name='vendor-create'),
    path('retrieve/<int:pk>/', VendorRetrieveApiView.as_view(),
         name='vendor-retrieve'),
    path('update/<int:pk>/', VendorUpdateApiView.as_view(),
         name='vendor-update'),
    path('delete/<int:pk>/', VendorDestroyApiView.as_view(),
         name='vendor-delete'),
    path('list/', VendorListApiView.as_view(),
         name='vendor-list'),
]
