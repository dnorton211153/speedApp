from django.apps import AppConfig


class SpeedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'speedApp'
    app_label = 'speedApp'
    def __str__(self):
        return self.name + ": " + str(self.app_label)