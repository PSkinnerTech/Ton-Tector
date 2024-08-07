import requests

TELEGRAM_TOKEN = '7102720922:AAF06M4xBfcRxrWWJx3KFWlAZsiiLH87h-Y'
WEBHOOK_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook'
response = requests.get(WEBHOOK_URL, params={'url': 'https://your_domain.com/webhook'})
print(response.json())