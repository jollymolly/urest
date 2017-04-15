from django.conf.urls import url, include
from rest_framework import routers

from .apps import UrestConfig
from .views import (YoutubeViewSet,
                    YoutubeDemographicsAnalyticsViewSet,)


app_name = UrestConfig.name

router = routers.DefaultRouter()
router.register(r'youtube', YoutubeViewSet, base_name='youtube')
router.register(r'youtube_demographics_analytics',
               YoutubeDemographicsAnalyticsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

