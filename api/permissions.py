from rest_framework.permissions import BasePermission
from django.core.exceptions import ObjectDoesNotExist

from api import models
from api import exceptions


class IsAdministrator(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsInterviewWasPassed(BasePermission):

    def has_permission(self, request, view):
        try:
            interview = models.InterviewDb.objects.get(id=request.POST.get('interview'))
        except ObjectDoesNotExist:
            return True

        interview_passings = models.InterviewPassingDb.objects.filter(user_id=request.POST.get('user_id'),
                                                                      question_id__in=list(
                                                                          interview.questions.values_list(
                                                                              'id'))).count()
        if interview_passings >= len(interview.questions.values_list('id')):
            raise exceptions.ErrorItWasPassed
        return True


class AnswerWasReceived(BasePermission):
    def has_permission(self, request, view):
        if models.InterviewPassingDb.objects.filter(user_id=request.POST.get('user_id'),
                                                    question_id=request.POST.get('question'),
                                                    interview_id=request.POST.get('interview')).count() > 0:
            raise exceptions.ErrorYouAnsweredThisQuestion
        return True
