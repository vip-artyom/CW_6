from django.urls import path, include
from ads.views import AdViewSet, CommentViewSet
from rest_framework_nested import routers


ads_router = routers.SimpleRouter()
ads_router.register('ads', AdViewSet, basename='ads')

comments_router = routers.NestedSimpleRouter(ads_router, r'ads', lookup='ad')
comments_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(ads_router.urls)),
    path('', include(comments_router.urls)),
]
