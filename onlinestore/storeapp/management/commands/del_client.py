from django.core.management.base import BaseCommand
from storeapp.models import Client


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ИД клиента')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = client.objects.filter(pk=pk).first()
        if client is not None:
            client.delete()
        self.stdout.write(f'{client}')