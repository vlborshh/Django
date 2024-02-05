from django.core.management.base import BaseCommand
from storeapp.models import Client

class Command(BaseCommand):
    def handle(self, *args, **options):
        client = Client(name_client='Петр',
                        phone_client='+7 987-654-32-21',
                        email_client='petr@mail.ru',
                        adress_client='Адрес где то там',
                        )
        client.save()