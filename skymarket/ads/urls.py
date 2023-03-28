from django.urls import path, include

from ads.views import AdViewSet
from rest_framework import routers

# TODO настройка роутов для модели

ads_router = routers.SimpleRouter()
ads_router.register('ads', AdViewSet, basename='ads')
# ads_router.register('ads/(?P<ad_id>[^/.]+)/comments', basename='comments')

urlpatterns = [
    path('', include(ads_router.urls)),
]
