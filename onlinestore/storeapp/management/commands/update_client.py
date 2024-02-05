from django.core.management.base import BaseCommand
from storeapp.models import Client

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ИД клиента')
        parser.add_argument('name_client', type=str, help='Имя клиента')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name_client')
        client = client.objects.filter(pk=pk).first()
        client.name_client = name
        client.save()
        self.stdout.write(f'{client}')