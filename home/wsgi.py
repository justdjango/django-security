import os
from django.conf import settings
from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home.settings")

application = get_wsgi_application()

# if not settings.DEBUG:
# application = DjangoWhiteNoise(application)
