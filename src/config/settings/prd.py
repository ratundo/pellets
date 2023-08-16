from config.settings.base import *  # NOQA

DEBUG = False

SECRET_KEY = "django-insecure-(r0d+yvyn+atl#k$8+ovofm6$$=w_pi^i*m)cfer1ujk16^e*!"

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
