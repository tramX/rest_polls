from rest_framework.exceptions import APIException


class ErrorCountAnswers(APIException):
    status_code = 400
    default_detail = 'Должен быть как минимум один вариант ответа'
    default_code = 'error_count_answers'


class ErrorOneCountAnswers(ErrorCountAnswers):
    default_detail = 'Должен быть всего один вариант ответ'


class ErrorTextAnswers(ErrorCountAnswers):
    default_detail = 'Не указан текстовый ответ'


class ErrorNotSelectAnswer(ErrorCountAnswers):
    default_detail = 'Вы не выбрали ответ'


class ErrorManySelectAnswer(ErrorCountAnswers):
    default_detail = 'Необходимо выбрать только один ответ'


class ErrorItWasPassed(ErrorCountAnswers):
    default_detail = 'Опрос уже пройден'


class ErrorYouAnsweredThisQuestion(ErrorCountAnswers):
    default_detail = 'Вы отвечали на этот вопрос'
