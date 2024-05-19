from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (UserListAPIView, UserUpdateAPIView,
                         UserRetrieveAPIView, UserCreateAPIView,
                         UserDestroyAPIView)

app_name = UsersConfig.name
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserListAPIView.as_view(), name='users_list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='users_update'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='users_view'),
    path('create/', UserCreateAPIView.as_view(), name='users_create'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='users_create'),
]