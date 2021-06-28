from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import client_serializers
from api import models
from api import exceptions
from api import permissions


class InterviewPassingCreate(generics.ListCreateAPIView):
    """
            Прохождение опроса пользователем и получения пройденных опросов с фильтрацией по id пользователя
    """

    queryset = models.InterviewPassingDb.objects.all()
    serializer_class = client_serializers.CreateInterviewPassingSerializer
    permission_classes = (permissions.IsInterviewWasPassed, permissions.AnswerWasReceived)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'user_id',
    )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        if (serializer._validated_data.get('question').question_type == models.TEXT_ANSWER and
                serializer._validated_data.get('text_answer') == ''):
            raise exceptions.ErrorTextAnswers
        elif (serializer._validated_data.get('question').question_type in [models.ONE_ANSWER, models.MANY_ANSWER] and
                len(serializer._validated_data.get('answers')) == 0):
            raise exceptions.ErrorNotSelectAnswer
        elif (serializer._validated_data.get('question').question_type == models.ONE_ANSWER and
                len(serializer._validated_data.get('answers')) > 1):
            raise exceptions.ErrorManySelectAnswer

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
