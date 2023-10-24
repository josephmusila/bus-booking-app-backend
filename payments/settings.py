from django.conf import settings
from rest_framework.settings import APISettings

USER_SETTINGS = getattr(settings, 'MPESA_CONFIG', None)

DEFAULTS = {
    'CONSUMER_KEY': 'WVxutTAJYYiccDCICWQjST1UXh0BupCA',
    'CONSUMER_SECRET': 'DAaA7fZhcutyWNzd',
    'CERTIFICATE_FILE': None,
    'HOST_NAME': "https://25aa-102-135-174-101.ngrok-free.app",
    'PASS_KEY': 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919',
    'SAFARICOM_API': 'https://sandbox.safaricom.co.ke',
    'AUTH_URL': '/oauth/v1/generate?grant_type=client_credentials',
    'SHORT_CODE': "174379",
    'TILL_NUMBER': "174379",
    'TRANSACTION_TYPE': 'CustomerBuyGoodsOnline',
}

api_settings = APISettings(USER_SETTINGS, DEFAULTS, None)
