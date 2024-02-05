from django.db import models
from django.core.validators import RegexValidator

# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента
class Client(models.Model):
    name_client = models.CharField(max_length=80)
    email_client = models.EmailField()
    phone_client = models.CharField(
                                    validators=[RegexValidator(r'^\d\d \d\d\d-\d\d\d-\d\d-\d\d')],
                                    max_length=12,
                                    null=False,
                                    help_text='Номер телефона должен быть введен в формате: +7 xxx-xxx-xx-xx')
    adress_client = models.CharField(max_length=180)
    date_client = models.DateField(auto_now_add=True)


# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
class Product(models.Model):
    name_product = models.CharField(max_length=80)
    text_product = models.TextField()
    price_product = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_product = models.IntegerField()
    date_product = models.DateField(auto_now_add=True)


# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
class Order(models.Model):
    client_order = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    product_order = models.ManyToManyField(Product)
    price_order = models.DecimalField(max_digits=10, decimal_places=2)
    date_order = models.DateField(auto_now_add=True)

