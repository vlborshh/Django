from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from storeapp.models import Client, Product, Order
from django.utils import timezone
import logging
from django.core.files.storage import FileSystemStorage
from storeapp.forms import ProductFormWidget


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

# Продолжаем работать с товарами и заказами.
#
# Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
# — за последние 7 дней (неделю)
# — за последние 30 дней (месяц)
# — за последние 365 дней (год)
#
# Товары в списке не должны повторятся.

def sorting_orders_date_duration(client_id, duration, title):
    products = []
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client_order=client,
                                  date_order__gt=(timezone.now() - timezone.timedelta(days=duration))).all()
    for order in orders:
        for product in order.product_order.all():
            products.append(product.name_product)
    products = set(products)
    context = {'title': title,
               'client_id': client_id,
               'items': products,
               }
    return context


# — за последние 7 дней (неделю)
def sorting_orders_date_week(request, client_id, duration=7):
    title = 'Сортировка за неделю'
    context = sorting_orders_date_duration(client_id, duration, title)
    return render(request, 'storeapp/sorting_orders_date.html', context)


# — за последние 30 дней (месяц)
def sorting_orders_date_month(request, client_id, duration=30):
    title = 'Сортировка за месяц'
    context = sorting_orders_date_duration(client_id, duration, title)
    return render(request, 'storeapp/sorting_orders_date.html', context)


# — за последние 365 дней (год)
def sorting_orders_date_year(request, client_id, duration=365):
    title = 'Сортировка за год'
    context = sorting_orders_date_duration(client_id, duration, title)
    return render(request, 'storeapp/sorting_orders_date.html', context)


# для любого периода
def sorting_orders_date(request, client_id, duration):

    day = ''
    title = ''

    if duration == 1:
        day = 'день'
    elif duration >= 2 and duration <= 4:
        day= 'дня'
    else:
        day = 'дней'

    title = f'Сортировка за период в {duration} {day}'
    context = sorting_orders_date_duration(client_id, duration, title)
    return render(request, 'storeapp/sorting_orders_date.html', context)

# Создайте форму, которая позволит сохранять фото.
def product_form_add(request):
    if request.method == 'POST':
        form = ProductFormWidget(request.POST, request.FILES)
        message = 'Вы ввели не верные данные. Исправьте ошибку'
        if form.is_valid():
            name_product = form.cleaned_data['name_product']
            text_product = form.cleaned_data['text_product']
            price_product = form.cleaned_data['price_product']
            quantity_product = form.cleaned_data['quantity_product']
            date_product = form.cleaned_data['date_product']
            image_product = form.cleaned_data['image_product']
            fs = FileSystemStorage()
            fs.save(image_product.name, image_product)
            logger.info(f'Получили {name_product}, {text_product}, {price_product}, '
                        f'{quantity_product}, {date_product}, фото загружено')
            product = Product(name_product=name_product, text_product=text_product, price_product=price_product,
                              quantity_product=quantity_product, date_product=date_product, image_product=image_product)
            product.save()
            message = 'Товар добавлен'
    else:
        form = ProductFormWidget()
        message = 'Добавление товара - заполните форму '
    context = {'title': 'Форма добавления товара',
               'form': form,
               'message': message,
               'name': 'product_form_add'}
    return render(request, 'storeapp/product_form_add.html', context)