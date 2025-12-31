from django.apps import AppConfig

class CommonUsersConfig(AppConfig):
    name = 'common_users'
    verbose_name = "Gestion des utilisateurs"
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import common_users.signals