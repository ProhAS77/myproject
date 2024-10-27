import logging
from django.shortcuts import render
from django.http import HttpResponse  # возвращает http-ответ от сервера к пользователю

logger = logging.getLogger(__name__)


def index(request): #request - объект запроса. Каждая функция получит свой объект запроса
    logger.info('Index page accessed')
    return HttpResponse('Hello word!')


def about(request):
    try:
        ...
        res = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse('Ooops, something went wrong')
    else:
        logger.debug('About page accessed')
        return HttpResponse('This is the about page')
