from django.apps import AppConfig


class ExcersiseConfig(AppConfig):
    name = 'excersise'

    def ready(self):
        import excersise.signals
