from django.apps import AppConfig

class CommonFrontendConfig(AppConfig):
    # Pas de default_auto_field car pas de modèle
    name = 'common_frontend'
    verbose_name = "Frontend Commun (Design)"