from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from ads.filters import AdFilter
from ads.models import Ad
from ads.serializers import AdSerializer, CommentSerializer, AdDetailSerializer, CommentCreateSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(ModelViewSet):
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_permissions(self):
        if self.action in 'list':
            self.permission_classes = [permissions.BasePermission]
        elif self.action in ['list', 'create', 'retrieve', 'me']:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AdDetailSerializer
        return AdSerializer

    def get_queryset(self):
        if self.action == 'me':
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    serializer_action_classes = {
        'list': CommentSerializer,
        'retrieve': CommentSerializer,
        'create': CommentCreateSerializer,
        'update': CommentCreateSerializer,
    }

    def get_permissions(self):
        if self.action in ['list', 'create', 'retrieve', 'me']:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    def get_queryset(self):
        ad_instance = get_object_or_404(Ad, id=self.kwargs['ad_pk'])
        return ad_instance.comment_set.all()

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def perform_create(self, serializer):
        ad = Ad.objects.get(pk=self.kwargs['ad_pk'])
        serializer.save(author=self.request.user, ad=ad)
