from rest_framework import permissions


class IsOwnerOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        # 로그인한 사용자인 경우 API 사용 가능
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # GET, OPTION, HEAD 요청일 때는 그냥 허용
        if request.method in permissions.SAFE_METHODS:
            return True
        # DELETE, PATCH 일 때는 현재 사용자와 객체가 참조 중인 사용자가 일치할 때만 허용
        return obj.myUser == request.user
