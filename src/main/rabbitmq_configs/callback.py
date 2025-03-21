import json
from src.drivers.telegram_sender import send_telegram_message

def rabbitmq_callback(ch, method, properties, body):
    msg = body.decode("utf-8")
    formatted_msg = json.loads(msg)
    # Transformando em dicionario
    telegram_message = formatted_msg["msg"]

    send_telegram_message(telegram_message)

    # Temos que tratar as mensagens que recebemos e fazemos isso com o callback
