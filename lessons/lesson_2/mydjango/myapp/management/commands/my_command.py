from typing import Any
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Print "Hello wordl!" to output'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write('Hello world!')