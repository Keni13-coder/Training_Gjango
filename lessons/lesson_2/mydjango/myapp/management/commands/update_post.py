from django.core.management.base import BaseCommand
from myapp.models import Post
from datetime import datetime

class Command(BaseCommand):
    help = 'Update Post'
    
    def add_arguments(self, parser) -> None:
        parser.add_argument('title', type=str, help='Post title')
        parser.add_argument('content', type=str, help='Post content')
        parser.add_argument('time', type=datetime, help='Post time')
        parser.add_argument('author', type=int, help='Post forgen author id')
        parser.add_argument('category', type=str, help='Post category')
        parser.add_argument('active', type=bool, help='Post category')
        
    def handle(self, pk: int, **field_model: dict) -> str | None:
        post = Post.objects.filter(pk=pk).first()
        if post:
            for key, value in field_model.items:
                if value:
                    setattr(post, key, value)
        self.stdout.write(f'{post}')