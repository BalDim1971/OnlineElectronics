from django.urls import path
from contacts.views import (ContactsListApiView, ContactsCreateApiView,
                            ContactsRetrieveApiView, ContactsUpdateApiView,
                            ContactsDestroyApiView)

urlpatterns = [
    path('create/', ContactsCreateApiView.as_view(),
         name='contacts-create'),
    path('retrieve/<int:pk>/', ContactsRetrieveApiView.as_view(),
         name='contacts-retrieve'),
    path('update/<int:pk>/', ContactsUpdateApiView.as_view(),
         name='contacts-update'),
    path('delete/<int:pk>/', ContactsDestroyApiView.as_view(),
         name='contacts-delete'),
    path('list/', ContactsListApiView.as_view(),
         name='contacts-list'),
]
