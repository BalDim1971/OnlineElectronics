from rest_framework.filters import SearchFilter
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView,
                                     ListAPIView)

from contacts.models import Contacts
from users.permissions import IsActive
from contacts.serializers import ContactsSerializer


class ContactsCreateApiView(CreateAPIView):
    serializer_class = ContactsSerializer
    permission_classes = [IsActive]


class ContactsRetrieveApiView(RetrieveAPIView):
    serializer_class = ContactsSerializer
    permission_classes = [IsActive]
    queryset = Contacts.objects.all()


class ContactsUpdateApiView(UpdateAPIView):
    serializer_class = ContactsSerializer
    permission_classes = [IsActive]
    queryset = Contacts.objects.all()


class ContactsDestroyApiView(DestroyAPIView):
    serializer_class = ContactsSerializer
    permission_classes = [IsActive]
    queryset = Contacts.objects.all()


class ContactsListApiView(ListAPIView):
    serializer_class = ContactsSerializer
    permission_classes = [IsActive]
    queryset = Contacts.objects.all()
    filter_backends = [SearchFilter]
