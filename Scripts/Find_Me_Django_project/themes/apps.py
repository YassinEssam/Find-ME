from django.apps import AppConfig


class ThemesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'themes'

# I will add themes hear 
# the next code could be wroted in any app but  I prefered to make a specific app for themes

# my_project_app/apps.py
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
    layout = 'vertical'
    layout = ''
