"""rest_polls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from api.views import admin_views
from api.views import client_views


admin_patterns = ([
    path('interview/', admin_views.InterviewCreate.as_view()),
    path('interview/<uuid:id>/', admin_views.InterviewDetail.as_view()),
    path('answer/', admin_views.AnswerCreate.as_view()),
    path('question/', admin_views.QuestionCreate.as_view()),
])

client_patterns = ([
    path('interview-passing/', client_views.InterviewPassingCreate.as_view()),
])


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-admin/', include(admin_patterns)),
    path('api-client/', include(client_patterns)),
]
