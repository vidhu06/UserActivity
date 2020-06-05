from rest_framework import serializers
from .models import User, ActivityPeriod

class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format = '%b %d %Y %H:%M%p')
    end_time = serializers.DateTimeField(format = '%b %d %Y %H:%M%p')
    class Meta:
        model = ActivityPeriod
        fields = ("start_time","end_time")

class UserActivitySerializer(serializers.ModelSerializer):
    activity_period = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ("id","real_name","tz","activity_period")

    def get_activity_period(self,instance):
        person_id = instance.id
        activity_list = ActivityPeriod.objects.filter(user__id = person_id)
        return ActivityPeriodSerializer(activity_list, many=True).data
    
