from django.conf import settings

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', "English"),
    ('ru', "russia"),
    ('uz', "Uzbek"),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'ru', 'uz')

USE_I18N = True

LOCALE_PATHS = [
    settings.BASE_DIR / 'locale',
]
