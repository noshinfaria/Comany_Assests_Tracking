from rest_framework import permissions


class IsCompanyEmployee(permissions.BasePermission):
    # Custom permission to only allow company employees to access an object.

    def has_object_permission(self, request, view, obj):
        return request.user.company == obj.company
