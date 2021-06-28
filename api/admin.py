from django.contrib import admin

from api.models import Question, InterviewDb, InterviewPassingDb


@admin.register(Question)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'interview',)


@admin.register(InterviewDb)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(InterviewPassingDb)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user_id',)
