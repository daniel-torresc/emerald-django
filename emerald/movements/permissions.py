from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdminReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = 'You do not have permission to edit this project type because you are not the owner'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # Permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user or request.user.is_staff
