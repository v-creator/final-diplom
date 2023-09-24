from django.apps import AppConfig


class BackendConfig(AppConfig):
    name = 'app'

    def ready(self):
        """
        импортируем сигналы
        """