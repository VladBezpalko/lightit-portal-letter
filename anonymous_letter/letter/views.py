from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import list_route
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from letter.filters import LetterFilter
from letter.models import Letter
from letter.permissions import LetterPermission
from letter.serializers import LetterCreateSerializer, LetterSerializer


class LetterViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.ListModelMixin, GenericViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = (LetterPermission, )
    filter_backends = (DjangoFilterBackend, )
    filter_class = LetterFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return LetterCreateSerializer

        return self.serializer_class

    @list_route(methods=['POST'])
    def check(self, request):
        codeword = self.request.data.get('codeword')

        instances = list(
            filter(
                lambda obj: obj.check_codeword(codeword),
                self.get_queryset()
            )
        )
        if len(instances) > 1:  # Main problem of this version
            raise RuntimeError('Similar codewords. Collision.')

        try:
            instance = instances[0]
        except KeyError:
            raise PermissionDenied('Id/codeword not correct')

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
