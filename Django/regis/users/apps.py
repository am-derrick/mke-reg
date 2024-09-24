from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'users'
def ready(self):
    import myapp.signals
