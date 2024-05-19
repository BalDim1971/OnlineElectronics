from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """
    Проверяет, активен ли пользователь.
    """
    message = "Пользователь - неактивен"

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active


class IsVerifiedUser(BasePermission):
    """
    Проверяет, есть ли у пользователя разрешение на доступ
    к запрашиваемому представлению.
    """
    def has_permission(self, request, view):
        # Проверяем, не является ли пользователь анонимным
        if not request.user.is_authenticated:
            return False
        elif request.user.is_authorized:
            return True
        raise PermissionDenied("Пользователь не авторизован или не прошел "
                               "проверку верификации")
