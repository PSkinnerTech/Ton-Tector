from flask import request, jsonify
import requests
from .models import User, db

def send_message(chat_id, text, config):
    url = f'https://api.tonfura.com/v1/bots/{config.TONX_BOT_ID}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    headers = {
        'Authorization': f'Bearer {config.TONX_API_KEY}',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=payload, headers=headers)

def handle_message(data, config):
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    
    if text == '/start':
        start(chat_id, config)
    elif text == '/subscribe':
        subscribe(chat_id, config)
    elif text == '/unsubscribe':
        unsubscribe(chat_id, config)
    elif text == '/status':
        status(chat_id, config)

def start(chat_id, config):
    user = User.query.filter_by(chat_id=chat_id).first()
    if not user:
        user = User(chat_id=chat_id, subscribed=True)
        db.session.add(user)
        db.session.commit()
    send_message(chat_id, 'Welcome! Use /subscribe to get updates and /unsubscribe to stop.', config)

def subscribe(chat_id, config):
    user = User.query.filter_by(chat_id=chat_id).first()
    if user:
        user.subscribed = True
        db.session.commit()
        send_message(chat_id, 'You have subscribed to updates.', config)
    else:
        send_message(chat_id, 'You need to /start first.', config)

def unsubscribe(chat_id, config):
    user = User.query.filter_by(chat_id=chat_id).first()
    if user:
        user.subscribed = False
        db.session.commit()
        send_message(chat_id, 'You have unsubscribed from updates.', config)
    else:
        send_message(chat_id, 'You need to /start first.', config)

def status(chat_id, config):
    user = User.query.filter_by(chat_id=chat_id).first()
    if user and user.subscribed:
        send_message(chat_id, 'You are subscribed to updates.', config)
    else:
        send_message(chat_id, 'You are not subscribed to updates.', config)