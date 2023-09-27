from django.core.management.base import BaseCommand
from myapp.models import Post



class Command(BaseCommand):
    help = 'Get all Post'
    
    def handle(self, **arwgs):
        post = Post.objects.all()
        self.stdout.write(f'{post}')