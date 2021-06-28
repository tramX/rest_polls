from rest_framework import serializers

from api.models import InterviewDb, Answer, Question


class CreateInterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterviewDb
        fields = '__all__'


class UpdateInterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterviewDb
        fields = [
            'id',
            'name',
            'description',
            'date_start',
            'date_end',
        ]
        read_only_fields = [
            'id',
            'date_start',
        ]


class CreateAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class CreateQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'