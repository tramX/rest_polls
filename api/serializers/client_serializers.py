from rest_framework import serializers

from api.models import InterviewPassingDb


class CreateInterviewPassingSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterviewPassingDb
        fields = '__all__'