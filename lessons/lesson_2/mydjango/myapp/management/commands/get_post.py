from typing import Any
from django.core.management.base import BaseCommand
from myapp.models import Post


class Command(BaseCommand):
    help = 'Get Post'
    
    
    def add_arguments(self, parser) -> None:
        parser.add_argument('pk', type=int, help='Post ID')
        
    def handle(self, *args: Any, **options: Any) -> str | None:
        # pk - первичный ключ
        pk = options['pk']
        post = Post.objects.filter(pk=pk).first()
        self.stdout.write(f'{post}')