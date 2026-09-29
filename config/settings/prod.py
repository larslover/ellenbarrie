from .base import *


# ============================================================
# PRODUCTION
# ============================================================

DEBUG = False


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