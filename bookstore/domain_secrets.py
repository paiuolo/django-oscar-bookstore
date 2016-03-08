DOMAIN_SECRET_KEY='m9+vr4ms0#g#9&!3^twq=j!yvmcgixn--_y+=hz*z63$y#uk3$'

DOMAIN_ALLOWED_HOSTS = ['.example.com',]

DOMAIN_TIME_ZONE = 'UTC'

DOMAIN_LANGUAGE_CODE = 'en'

gettext_noop = lambda s: s
DOMAIN_LANGUAGES = [
    ('en-us', gettext_noop('English')),
]

DOMAIN_SHOP_NAME = 'Oscar bookstore'
DOMAIN_SHOP_TAGLINE = 'Bookstore'

DOMAIN_DEFAULT_CURRENCY = 'EUR'

DOMAIN_INFO_EMAIL = 'info@example.com'


# bookstore
NEW_PRODUCT_DAYS = 30
CELERY_IS_ACTIVE = False
SEND_ORDER_VIA_EMAIL = False
CHECK_TWIN_DIGITAL_PRODUCTS = False