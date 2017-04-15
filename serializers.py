from chanalytics.models import (Youtube,
                                DemographicsAnalytics)

from rest_framework import serializers

class YoutubeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Youtube
        fields = ('id', 'name', 'title', 'rank',)

class YoutubeDemographicsAnalyticsSerializer(
        serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = DemographicsAnalytics
        fields = ('id', 'age_group', 'gender', 'viewer_percentage',)
        
