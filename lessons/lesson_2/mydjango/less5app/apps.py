from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class Less5AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'less5app'
    verbose_name = _("Товары и категории")