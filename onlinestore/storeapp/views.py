from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    html = '<h1>Главная страница</h1><p>что то тут написано</p><p>и тут </p>'
    logger.info('Открыта главная страница')
    return HttpResponse(html)


def about(request):
    html = '<h1>Страница о "..."</h1><p>что то тут написано</p><p>и тут </p>'
    logger.info(f'Открыта страница about')
    return HttpResponse(html)
