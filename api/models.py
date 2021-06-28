from django.db import models
import uuid

TEXT_ANSWER = 'text_answer'
ONE_ANSWER = 'one_answer'
MANY_ANSWER = 'many_answer'

QUESTION_TYPES = (
    (TEXT_ANSWER, TEXT_ANSWER),
    (ONE_ANSWER, ONE_ANSWER),
    (MANY_ANSWER, MANY_ANSWER)
)


class BaseDb(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class InterviewDb(BaseDb):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.name


class Answer(BaseDb):
    text = models.TextField()

    def __str__(self):
        return self.text


class Question(BaseDb):
    name = models.CharField(max_length=255)
    question_type = models.CharField(max_length=255, choices=QUESTION_TYPES)
    interview = models.ForeignKey(
        InterviewDb,
        related_name='questions',
        on_delete=models.CASCADE
    )
    answers = models.ManyToManyField(Answer, blank=True)

    def __str__(self):
        return self.name


class InterviewPassingDb(BaseDb):
    user_id = models.PositiveIntegerField()
    interview = models.ForeignKey(
        InterviewDb,
        related_name='interview_passings',
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question,
        related_name='questions',
        on_delete=models.CASCADE
    )
    text_answer = models.TextField(blank=True)
    answers = models.ManyToManyField(Answer, blank=True)

    def __str__(self):
        return f'${self.interview} ${self.user_id}'
