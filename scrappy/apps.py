from django.apps import AppConfig
from .cron import start

class ScrappyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scrappy'

    def ready(self):
        start()
