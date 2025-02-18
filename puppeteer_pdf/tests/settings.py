import os

DIRNAME = os.path.abspath(os.path.dirname(__file__))
DEBUG = False
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "puppeteer_pdf.tests",
    "puppeteer_pdf",
)
MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
)
MEDIA_ROOT = os.path.join(DIRNAME, "media")
MEDIA_URL = "/media/"
STATIC_ROOT = os.path.join(DIRNAME, "static")
STATIC_URL = "/static/"
TEMPLATES = [  # For Django >= 1.10. Ignored in lower versions
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": [],
        "OPTIONS": {},
    },
]
PUPPETEER_PDF_DEBUG = True
PUPPETEER_PDF_URL = "http://django-puppeteer-pdf-service:3020"
