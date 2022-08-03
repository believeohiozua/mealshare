from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_authenticated and user.is_admin
