import os
import sys

from config.settings.base import *  # NOQA

DEBUG = True

SECRET_KEY = "django-secret-key"

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "*"]

INSTALLED_APPS += []

if os.environ.get("GIHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "0.0.0.0",
            "PORT": 5432,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": os.environ.get("POSTGRES_PORT"),
        }
    }
if "test" in sys.argv or os.environ.get("DJANGO_SETTINGS_MODULE") == "config.settings.dev":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# if "test" in sys.argv or "test_coverage" in sys.argv:
#     # Disable GDAL for tests
#     DATABASES["default"]["ENGINE"] = "django.db.backends.sqlite3"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = "static/"
# STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "static/"  # NOQA

MEDIA_ROOT = BASE_DIR / "media/"  # NOQA
MEDIA_URL = "/media/"

GRAPH_MODELS = {
    "app_labels": ["main", "goods", "logistics", "inquiry", "offer"],
}
