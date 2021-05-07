from django.apps import AppConfig


class PetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pets'
    verbose_name = '寵物'
    verbose_name_plural = '寵物'
