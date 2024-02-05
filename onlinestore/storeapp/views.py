from django.shortcuts import render
from django.http import HttpResponse
from storeapp.models import Client, Product, Order
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


def clients(request):
    logger.info(f'Открыта страница clients')
    client = Client.objects.all()
    result = ''
    for item in client:
        result += '<br>' + item.name_client + ' ' + item.phone_client + ' ' + item.email_client + ' ' + item.adress_client
    return HttpResponse(f'Список всех клиентов:{result}')


def product(request):
    logger.info(f'Открыта страница product')
    product = Product.objects.all()
    result = ''
    for item in product:
        result += '<br>' + item.name_product + ' ' + str(item.quantity_product) + ' ' + str(item.price_product)
    return HttpResponse(f'Список всех товаров:{result}')


def order(request):
    logger.info(f'Открыта страница order')
    order = Order.objects.all()
    return HttpResponse(order)

