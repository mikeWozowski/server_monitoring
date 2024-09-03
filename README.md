# Server Monitoring with Telegram Notifications

## Описание

Этот проект отслеживает загрузку процессора сервера и отправляет уведомления в Telegram при превышении заданного порога.

## Требования

- Docker

## Установка и запуск

1. **Создайте Telegram-бота** и получите токен от `BotFather`.
2. **Получите идентификатор чата** для вашего Telegram-канала или чата.

3. **Клонируйте репозиторий**:

   ```bash
   git clone https://github.com/mikeWozowski/server_monitoring.git
   cd server_monitoring
   ```

4. **Соберите Docker-образ**:

   ```bash
   docker build -t server-monitor .
   ```

5. **Запустите контейнер**, передав переменные окружения:

   ```bash
   docker run -d --name server-monitor \
     -e TELEGRAM_TOKEN=ВАШ_ТОКЕН_БОТА \
     -e CHAT_ID=ВАШ_CHAT_ID \
     server-monitor
   ```

## Конфигурация

- **`CPU_THRESHOLD`**: Порог загрузки процессора в процентах (по умолчанию 90%).
- **`CHECK_INTERVAL`**: Интервал проверки загрузки CPU в секундах (по умолчанию 60 секунд).
