from .base import *
import os


# ============================================================
# PRODUCTION
# ============================================================

DEBUG = False


# ============================================================
# SECRET KEY
# ============================================================

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")


# ============================================================
# ALLOWED HOSTS
# ============================================================

ALLOWED_HOSTS = [
    "ellenbarriechildren.com",
    "www.ellenbarriechildren.com",
]


# ============================================================
# CSRF
# ============================================================

CSRF_TRUSTED_ORIGINS = [
    "https://ellenbarriechildren.com",
    "https://www.ellenbarriechildren.com",
]


# ============================================================
# SECURITY
# ============================================================

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True