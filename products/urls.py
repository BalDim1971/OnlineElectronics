from django.urls import path
from products.views import (ProductListApiView, ProductCreateApiView,
                            ProductRetrieveApiView, ProductUpdateApiView,
                            ProductDestroyApiView)

urlpatterns = [
    path('create/', ProductCreateApiView.as_view(),
         name='products-create'),
    path('retrieve/<int:pk>/', ProductRetrieveApiView.as_view(),
         name='products-retrieve'),
    path('update/<int:pk>/', ProductUpdateApiView.as_view(),
         name='products-update'),
    path('delete/<int:pk>/', ProductDestroyApiView.as_view(),
         name='products-delete'),
    path('list/', ProductListApiView.as_view(),
         name='products-list'),
]
