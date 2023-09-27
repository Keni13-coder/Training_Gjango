from typing import Any
from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = 'Get user'
    
    
    def add_arguments(self, parser) -> None:
        parser.add_argument('pk', type=int, help='User ID')
        
    def handle(self, *args: Any, **options: Any) -> str | None:
        # pk - первичный ключ
        pk = options['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')