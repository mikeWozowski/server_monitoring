import psutil
import requests
import time
import os


# Настройки
CPU_THRESHOLD = 90  # Порог загрузки CPU в процентах
CHECK_INTERVAL = 60  # Интервал проверки в секундах
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')  # Токен бота из переменной окружения
CHAT_ID = os.getenv('CHAT_ID')  # ID чата из переменной окружения

def send_telegram_message(message):
    """Функция для отправки сообщения в Telegram."""
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f'Ошибка отправки сообщения: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'Ошибка подключения к Telegram: {e}')

def check_cpu_load():
    """Функция для проверки загрузки CPU."""
    cpu_load = psutil.cpu_percent(interval=1)
    if cpu_load > CPU_THRESHOLD:
        message = f'Внимание! Загрузка CPU: {cpu_load}%'
        send_telegram_message(message)

if __name__ == '__main__':
    while True:
        check_cpu_load()
        time.sleep(CHECK_INTERVAL)
