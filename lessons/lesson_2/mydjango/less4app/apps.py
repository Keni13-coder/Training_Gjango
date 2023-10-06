from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class Less4AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'less4app'
    verbose_name = _("Коментарии")
