import sys

from django.db.backends.sqlite3 import base

from config.settings.base import *  # NOQA

DEBUG = True

SECRET_KEY = "django-secret-key"

ALLOWED_HOSTS = ["127.0.0.1", "*"]

INSTALLED_APPS += []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if "test" in sys.argv or "test_coverage" in sys.argv:
    # Disable GDAL for tests
    DATABASES["default"]["ENGINE"] = "django.db.backends.sqlite3"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

GRAPH_MODELS = {
    "app_labels": ["main", "goods", "logistics", "inquiry", "offer"],
}
