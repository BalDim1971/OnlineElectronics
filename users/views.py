from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.permissions import IsStaff, IsActive
from users.serializers import UserSerializer, MyTokenObtainPairSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя"""
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        """Переопределение метода для сохранения хешированного пароля в бд
        (если пароль не хешируется - пользователь не считается активным и
        токен авторизации не создается)"""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class UserUpdateAPIView(generics.UpdateAPIView):
    """Обновление данных пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    
    def perform_update(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class UserListAPIView(generics.ListAPIView):
    """Отображение списка пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    permission_classes = [IsAuthenticated, IsStaff | IsActive]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Подробные данные пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsStaff | IsActive]


class UserDestroyAPIView(generics.DestroyAPIView):
    """Удаление данных пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
