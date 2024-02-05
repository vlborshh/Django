from django.core.management.base import BaseCommand
from storeapp.models import Client, Product, Order
import random

class Command(BaseCommand):

    def handle(self, *args, **options):


        for i in range(10):
            count = i + 1
            client = Client(name_client=f'Имя{count}',
                            phone_client=f'+7 987-654-32-1{i}',
                            email_client=f'mail{count}@mail.ru',
                            adress_client=f'Адрес {count}',
            )
            client.save()


        for i in range(1, 20):
            price = i * 0.01 * random.randint(1, 40000)
            count = i * random.randint(1, 1000)
            product = Product(name_product=f'Название продукта {i}',
                            text_product=f'Описание продукта {i}',
                            price_product=f'{price}',
                            quantity_product=f'{count}',
            )
            product.save()


        product = Product.objects.all()
        client = Client.objects.all()

        for _ in range(5):
            sum_order = 0
            order = Order(client_order=random.choice(client),
                          price_order=sum_order,
            )
            order.save()
            for _ in range(random.randint(1, 5)):
                order_product = random.choice(product)
                sum_order += order_product.price_product
                order.product_order.add(order_product)
                order.save()
            order.price_order = sum_order
            order.save()