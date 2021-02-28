from rest_framework import serializers

from .models.challenge import Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('id', 'title', 'start_date')


class ChallengesListSerializer(serializers.Serializer):
    class Meta:
        title = serializers.CharField(max_length=100)
        page_name = serializers.CharField(max_length=100)
        challenges = ChallengeSerializer()
