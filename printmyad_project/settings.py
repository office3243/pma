import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'zomk3t1=xvj*0__tbhgh)9kr)ym)mb&f8mmx0=i*8z#x-trek&'
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',

    "portal",
    "accounts",
    "campaigns",
    "industries",
    "localities",
    "payments",
    "stations",
    "dealers",
    "rates",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'printmyad_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'printmyad_project.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#   CUSTOM SETTINGS

AUTH_USER_MODEL = "accounts.User"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False



#   CUSTOM SETTINGS

STATIC_URL = '/static/'

STATIC_ROOR = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")


from django.urls import reverse_lazy

LOGIN_URL = reverse_lazy("accounts:login")
LOGIN_REDIRECT_URL = reverse_lazy("portal:home")
CRISPY_TEMPLATE_PACK = "bootstrap4"
SITE_DOMAIN = "http://127.0.0.1:8000"
API_KEY_2FA = "c9ef2a2e-806a-11e9-ade6-0200cd936042"


#   PAYTM LIVE
# PAYTM_MERCHANT_KEY = "xt94GuDiIMz_#84O"
# PAYTM_MERCHANT_ID = "ZIHCDc43188965988448"
PAYTM_WEBSITE = 'DEFAULT'
PAYTM_CALLBACK_URL = SITE_DOMAIN + "/payments/paytm/response/"

#   PAYTM TEST

PAYTM_MERCHANT_KEY = "mhTAUyOuhW752G_q"
PAYTM_MERCHANT_ID = "VgBKhn41304614600778"

#   EMAIL CREDENTIALS

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "webprintmyad@gmail.com"
EMAIL_HOST_PASSWORD = "Admin@2018#"

ADMIN_EMAIL = "office3243@gmail.com"
EMAIL_FROM = EMAIL_HOST_USER