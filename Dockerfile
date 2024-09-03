# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем необходимые пакеты
RUN pip install psutil requests

# Копируем скрипт мониторинга в контейнер
COPY monitor.py /app/monitor.py

# Устанавливаем рабочую директорию
WORKDIR /app

# Определяем команду запуска
CMD ["python", "monitor.py"]
