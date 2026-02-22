from rest_framework import serializers
from .models import Activity, Milestone


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['user', 'created_at']


class MilestoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milestone
        fields = '__all__'