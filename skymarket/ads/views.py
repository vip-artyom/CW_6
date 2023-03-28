from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from ads.filters import AdFilter
from ads.models import Ad
from ads.serializers import AdSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    serializer_class = AdSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    permission_classes = []

    def get_permissions(self):
        if self.action in ['list', 'create', 'retrieve', 'me']:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    def get_queryset(self):
        if self.action == 'me':
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    # @action(detail=False, methods=['get'], url_path=r'me', serializer_class=AdListSerializer)
    # def user_ads(self, request, *args, **kwargs):
    #     current_user = self.request.user
    #     user_ads = Ad.objects.filter(author=current_user)
    #     page = self.paginate_queryset(user_ads)
    #
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    # #
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
    #
    # def get_serializer_class(self):
    #     try:
    #         return self.serializer_action_classes[self.action]
    #     except (KeyError, AttributeError):
    #         return super().get_serializer_class()


# class CommentViewSet(ModelViewSet):
#     serializer_class = CommentSerializer
#     serializer_action_classes = {
#         'list': CommentListSerializer,
#         'retrieve': CommentListSerializer,
#         'create': CommentCreateSerializer,
#         'update': CommentCreateSerializer,
# #     }
#
#     # permission_classes = (UserPermissions,)
#
#     def get_queryset(self):
#         return Comment.objects.filter(ad_id=self.kwargs['ad_id'])
#
#     def get_serializer_class(self):
#         try:
#             return self.serializer_action_classes[self.action]
#         except (KeyError, AttributeError):
#             return super().get_serializer_class()
#
#     def perform_create(self, serializer):
#         ad = Ad.objects.get(pk=self.kwargs['ad_id'])
#         serializer.save(author=self.request.user, ad=ad)
