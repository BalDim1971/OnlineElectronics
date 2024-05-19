from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView,
                                     ListAPIView)

from contacts.models import Contacts
from users.permissions import IsActive
from contacts.serializers import ContactsSerializer


class ContactsListApiView(ListAPIView):
    """Список контактов"""
    serializer_class = ContactsSerializer
    permission_classes = [IsActive]
    queryset = Contacts.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)


class ContactsCreateApiView(CreateAPIView):
    """Создать контакт"""
    serializer_class = ContactsSerializer
    permission_classes = [IsActive]


class ContactsRetrieveApiView(RetrieveAPIView):
    """Подробные данные о контакте"""
    serializer_class = ContactsSerializer
    permission_classes = [IsActive]
    queryset = Contacts.objects.all()


class ContactsUpdateApiView(UpdateAPIView):
    """Обновить данные о контакте"""
    serializer_class = ContactsSerializer
    permission_classes = [IsActive]
    queryset = Contacts.objects.all()


class ContactsDestroyApiView(DestroyAPIView):
    """Удалить данные о контакте"""
    serializer_class = ContactsSerializer
    permission_classes = [IsActive]
    queryset = Contacts.objects.all()
