import requests

def send_telegram_message(message):
    token = "7648863719:AAF55RLpzz4Sm_pYV1NLWNHFVooTbuCrMWM"
    chat_id = "-1002423195944"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=payload)
    # Estamos mandando essa requisição para a url

