from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allows any user to read data (GET, HEAD, OPTIONS).
    Restricts write actions (POST, PUT, PATCH, DELETE) to Admin users only.
    """
    def has_permission(self, request, view):
        # Allow open read-only access for menu viewing
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # Require active authentication and Admin role status for modifications
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.role == 'admin'
        )