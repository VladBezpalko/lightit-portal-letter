from rest_framework.permissions import BasePermission


class LetterPermission(BasePermission):

    def has_permission(self, request, view):
        if view.action in ('partial_update', 'list'):
            return request.user.is_staff  # specialization == 'Boss'

        return view.action in ('create', 'check')
