from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
from users.permissions import IsVerifiedUser
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()


class UserListAPIView(generics.ListAPIView):
    """Отображение списка пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Обновление данных пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsVerifiedUser]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Подробные данные пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Удаление данных пользователя"""

    queryset = User.objects.all()
    permission_classes = [IsVerifiedUser]
