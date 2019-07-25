# ตามวิดีโอ ไฟล์นี้จะชื่อ permissions.py
# แต่สร้างให้ชื่อ มัน Unique หน่อยจะดีกว่า !!

from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        # permissions for read-only request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Dupplicate check and Obj.id == request.user.id Only !!
        return (obj.id == request.user.id)



# NOTE ::
# ------------------------------------------------------------------------------
# Document
# https://www.django-rest-framework.org/api-guide/permissions/
# POST            requests require the user to have the add permission on the model instance.
# PUT and PATCH   requests require the user to have the change permission on the model instance.
# DELETE          requests require the user to have the delete perm

# Example
# https://www.programcreek.com/python/example/71197/rest_framework.permissions.SAFE_METHODS
