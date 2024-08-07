from flask import request, jsonify
from app import app
import requests

TELEGRAM_TOKEN = '7102720922:AAF06M4xBfcRxrWWJx3KFWlAZsiiLH87h-Y'
WEBHOOK_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook'
WEBHOOK_PATH = '/webhook'

@app.route(WEBHOOK_PATH, methods=['POST'])
def telegram_webhook():
    update = request.json
    if 'message' in update:
        chat_id = update['message']['chat']['id']
        text = update['message']['text']
        if text == '/start':
            send_message(chat_id, 'Welcome to Ton-Tector!')
        elif text == '/data':
            data = fetch_tonx_data()
            send_message(chat_id, f'TonX Data: {data}')
        else:
            send_message(chat_id, f'You said: {text}')
    return 'ok', 200

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot7102720922:AAF06M4xBfcRxrWWJx3KFWlAZsiiLH87h-Y
/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

def fetch_tonx_data():
    tonx_api_url = 'https://api.tonx.com/data'  # Replace with actual endpoint
    response = requests.get(tonx_api_url)
    return response.json()