from rest_framework import permissions


class IsAdminOrAuthenticated(permissions.BasePermission):
    """
    Global permission to let only admin-type users update data
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True if request.user.is_authenticated else False
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False
