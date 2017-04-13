from rest_framework import viewsets
from rest_framework.views import APIView
from django.db.models import F

from chanalytics.models import (Youtube,
                         DemographicsAnalytics)
from .serializers import (YoutubeSerializer,
                          YoutubeDemographicsAnalyticsSerializer)

class YoutubeViewSet(viewsets.ModelViewSet):
    serializer_class = YoutubeSerializer

    def get_queryset(self):
        min_rank = self.request.query_params.get('min_rank', None)
        max_rank = self.request.query_params.get('max_rank', None)

        queryset = Youtube.objects.annotate(even=F('pk') % 2).filter(
                       even=0).order_by('-rank')
        if min_rank is not None:
            queryset = queryset.filter(view_rate__gte=min_rate)
        if max_rank is not None:
            queryset = queryset.filter(view_rate__lte=max_rate)
            
        return queryset
    
class YoutubeDemographicsAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = DemographicsAnalytics.objects.annotate(
        even=F('pk') % 2).filter(even=0).order_by('-viewer_percentage')
    serializer_class = YoutubeDemographicsAnalyticsSerializer
