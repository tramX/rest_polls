from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from api.permissions import IsAdministrator
from api.serializers import admin_serializers
from api import models
from api import exceptions


class InterviewCreate(generics.ListCreateAPIView):
    """
        Добавление опроса администратором
    """
    queryset = models.InterviewDb.objects.all()
    serializer_class = admin_serializers.CreateInterviewSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdministrator)


class InterviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
            Редактирование опроса администратором
    """
    queryset = models.InterviewDb.objects.all()
    serializer_class = admin_serializers.UpdateInterviewSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdministrator)
    lookup_field = 'id'


class AnswerCreate(generics.ListCreateAPIView):
    """
            Добавление ответов на вопросы
    """
    queryset = models.Answer.objects.all()
    serializer_class = admin_serializers.CreateAnswerSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdministrator)


class QuestionCreate(generics.ListCreateAPIView):
    """
            Добавление вопроса к опросу
    """

    queryset = models.Question.objects.all()
    serializer_class = admin_serializers.CreateQuestionSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdministrator)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if (serializer._validated_data.get('question_type') != models.TEXT_ANSWER and
                len(serializer._validated_data.get('answers')) == 0):
            raise exceptions.ErrorCountAnswers

        elif (serializer._validated_data.get('question_type') == models.ONE_ANSWER and
                len(serializer._validated_data.get('answers')) > 1):
            raise exceptions.ErrorOneCountAnswers

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
