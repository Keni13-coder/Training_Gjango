from django.core.management.base import BaseCommand
from myapp.models import Post



class Command(BaseCommand):
    help = 'Create post'
    
    
    def add_arguments(self, parser) -> None:
        parser.add_argument('title', type=str, help='Post title')
        parser.add_argument('content', type=str, help='Post content')
        parser.add_argument('author', type=int, help='Post forgen author id')
        parser.add_argument('category', type=str, help='Post category')
        
        
    def handle(self, **kwargs):
        # post = Post(name='John', email='john@example.com',
        #             password='secret', age=25)
        post = Post(**kwargs)
        post.save()
        self.stdout.write(f'{post}')
        # self.stdout.write(f'OK')