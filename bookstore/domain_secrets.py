SECRET_KEY='m9+vr4ms0#g#9&!3^twq=j!yvmcgixn--_y+=hz*z63$y#uk3$'

ALLOWED_HOSTS = ['.example.com',]

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en'

gettext_noop = lambda s: s
LANGUAGES = [
    ('en-us', gettext_noop('English')),
]

SHOP_NAME = 'Oscar bookstore'
SHOP_TAGLINE = 'Bookstore'

DEFAULT_CURRENCY = 'EUR'

INFO_EMAIL = 'info@example.com'


# bookstore
NEW_PRODUCT_DAYS = 30
CELERY_IS_ACTIVE = False
SEND_ORDER_VIA_EMAIL = False
CHECK_TWIN_DIGITAL_PRODUCTS = False