# API Reference - Low Code API Lib SDK v0.1.1

Это справочник по API для Low Code API Lib SDK версии 0.1.1.

## Содержание

- [Клиент SDK](#клиент-sdk)
- [Базовый API](#базовый-api)
- [API модули](#api-модули)
- [Обработка ошибок](#обработка-ошибок)
- [Сетевые возможности](#сетевые-возможности)
- [Примеры использования](#примеры-использования)

## Клиент SDK

### Client

Основной класс для работы с API.

```python
from my_sdk import Client

client = Client(
    token="your_api_token",
    base_url="https://api.example.com"  # опционально
)
```

#### Параметры:
- `token` (str): API токен для аутентификации
- `base_url` (str, optional): Базовый URL API. По умолчанию: "https://api.lowcodeapi.ru"

#### Доступные API модули:
- `client.auth` - AuthAPI для работы с аутентификацией
- `client.users` - UserAPI для работы с пользователями
- `client.bots` - BotsAPI для работы с ботами
- `client.files` - FilesAPI для работы с файлами
- `client.messages` - MessagesAPI для работы с сообщениями
- `client.webhooks` - WebhooksAPI для работы с вебхуками

## Базовый API

### BaseAPI

Базовый класс для всех API модулей.

```python
from my_sdk.base import BaseAPI

api = BaseAPI(token="your_token", base_url="https://api.example.com")
response = api.request("GET", "/endpoint")
```

#### Методы:
- `request(method, endpoint, **kwargs)` - Выполнить HTTP запрос
- `get(endpoint, **kwargs)` - GET запрос
- `post(endpoint, **kwargs)` - POST запрос
- `put(endpoint, **kwargs)` - PUT запрос
- `delete(endpoint, **kwargs)` - DELETE запрос

## API модули

### AuthAPI

Модуль для работы с аутентификацией.

```python
# Получить информацию о текущем пользователе
user_info = client.auth.get_me()

# Обновить токен
new_token = client.auth.refresh_token(refresh_token)
```

### UserAPI

Модуль для работы с пользователями.

```python
# Получить список пользователей
users = client.users.get_users()

# Получить пользователя по ID
user = client.users.get_user(user_id)

# Создать пользователя
new_user = client.users.create_user({
    "name": "John Doe",
    "email": "john@example.com"
})

# Обновить пользователя
updated_user = client.users.update_user(user_id, {"name": "Jane Doe"})

# Удалить пользователя
client.users.delete_user(user_id)
```

### BotsAPI

Модуль для работы с ботами.

```python
# Получить список ботов
bots = client.bots.get_bots()

# Получить бота по ID
bot = client.bots.get_bot(bot_id)

# Создать бота
new_bot = client.bots.create_bot({
    "name": "My Bot",
    "description": "Bot description"
})

# Обновить бота
updated_bot = client.bots.update_bot(bot_id, {"name": "Updated Bot"})

# Удалить бота
client.bots.delete_bot(bot_id)
```

### FilesAPI

Модуль для работы с файлами.

```python
# Загрузить файл
with open("file.txt", "rb") as f:
    uploaded_file = client.files.upload_file(f)

# Получить информацию о файле
file_info = client.files.get_file(file_id)

# Скачать файл
file_content = client.files.download_file(file_id)

# Удалить файл
client.files.delete_file(file_id)
```

### MessagesAPI

Модуль для работы с сообщениями.

```python
# Отправить сообщение
message = client.messages.send_message({
    "recipient_id": "user123",
    "text": "Hello, World!"
})

# Получить сообщения
messages = client.messages.get_messages()

# Получить сообщение по ID
message = client.messages.get_message(message_id)

# Удалить сообщение
client.messages.delete_message(message_id)
```

### WebhooksAPI

Модуль для работы с вебхуками.

```python
# Создать вебхук
webhook = client.webhooks.create_webhook({
    "url": "https://example.com/webhook",
    "events": ["message.sent", "user.created"]
})

# Получить список вебхуков
webhooks = client.webhooks.get_webhooks()

# Получить вебхук по ID
webhook = client.webhooks.get_webhook(webhook_id)

# Обновить вебхук
updated_webhook = client.webhooks.update_webhook(webhook_id, {
    "events": ["message.sent"]
})

# Удалить вебхук
client.webhooks.delete_webhook(webhook_id)
```

## Обработка ошибок

SDK предоставляет специализированные исключения для различных типов ошибок:

```python
from my_sdk.exceptions import (
    SDKError, AuthenticationError, NetworkError, 
    ValidationError, TimeoutError, RateLimitError
)

try:
    response = client.users.get_user("invalid_id")
except AuthenticationError as e:
    print(f"Ошибка аутентификации: {e}")
except ValidationError as e:
    print(f"Ошибка валидации: {e}")
except NetworkError as e:
    print(f"Сетевая ошибка: {e}")
except RateLimitError as e:
    print(f"Превышен лимит запросов: {e}")
except SDKError as e:
    print(f"Общая ошибка SDK: {e}")
```

### Типы исключений:

- `SDKError` - Базовое исключение SDK
- `AuthenticationError` - Ошибки аутентификации (401, 403)
- `ValidationError` - Ошибки валидации данных (400, 422)
- `NetworkError` - Сетевые ошибки
- `TimeoutError` - Ошибки таймаута
- `RateLimitError` - Превышение лимита запросов (429)
- `ServerError` - Серверные ошибки (5xx)

### Утилиты для обработки ошибок:

```python
from my_sdk.exceptions import handle_http_error, validate_token, validate_base_url

# Обработка HTTP ответа
response = requests.get("https://api.example.com/users")
handle_http_error(response)  # Выбросит соответствующее исключение при ошибке

# Валидация токена
validate_token("your_token")  # Выбросит ValidationError если токен невалиден

# Валидация базового URL
validate_base_url("https://api.example.com")  # Выбросит ValidationError если URL невалиден
```

## Сетевые возможности

### NetworkManager

Класс для управления HTTP соединениями с поддержкой повторных попыток и пулинга соединений.

```python
from my_sdk.network import NetworkManager

manager = NetworkManager(
    base_url="https://api.example.com",
    timeout=30,
    max_retries=3
)

# Выполнить запрос
response = manager.get("/users")

# Закрыть соединение
manager.close()
```

### NetworkSharing

Класс для создания сетевого сервера и клиента для обмена данными.

```python
from my_sdk.network import NetworkSharing

# Создать сервер
server = NetworkSharing(host="localhost", port=8080)
server.start_server()  # Запустить в отдельном потоке

# Подключиться к серверу
client_socket = server.connect_to_server("localhost", 8080)

# Отправить сообщение
server.send_message(client_socket, {"type": "hello", "data": "world"})

# Широковещательная отправка
server.broadcast_message({"type": "broadcast", "data": "message to all"})

# Остановить сервер
server.stop_server()
```

### Глобальные функции для управления соединениями:

```python
from my_sdk.network import get_network_manager, close_all_connections

# Получить менеджер сети (с пулингом соединений)
manager = get_network_manager("https://api.example.com")

# Закрыть все соединения
close_all_connections()
```

## Примеры использования

### Базовое использование

```python
from my_sdk import Client
from my_sdk.exceptions import SDKError

# Инициализация клиента
client = Client(token="your_api_token")

try:
    # Получить информацию о текущем пользователе
    user_info = client.auth.get_me()
    print(f"Привет, {user_info['name']}!")
    
    # Получить список пользователей
    users = client.users.get_users()
    print(f"Всего пользователей: {len(users)}")
    
    # Создать нового пользователя
    new_user = client.users.create_user({
        "name": "Test User",
        "email": "test@example.com"
    })
    print(f"Создан пользователь: {new_user['id']}")
    
except SDKError as e:
    print(f"Ошибка SDK: {e}")
```

### Работа с файлами

```python
from my_sdk import Client

client = Client(token="your_api_token")

# Загрузить файл
with open("document.pdf", "rb") as file:
    uploaded_file = client.files.upload_file(file)
    print(f"Файл загружен: {uploaded_file['id']}")

# Скачать файл
file_content = client.files.download_file(uploaded_file['id'])
with open("downloaded_document.pdf", "wb") as file:
    file.write(file_content)
```

### Работа с вебхуками

```python
from my_sdk import Client

client = Client(token="your_api_token")

# Создать вебхук
webhook = client.webhooks.create_webhook({
    "url": "https://myapp.com/webhook",
    "events": ["user.created", "message.sent"]
})

print(f"Вебхук создан: {webhook['id']}")
```

### Использование сетевых возможностей

```python
from my_sdk.network import NetworkSharing
import threading
import time

# Создать сервер
server = NetworkSharing(port=9000)

# Запустить сервер в отдельном потоке
server_thread = threading.Thread(target=server.start_server)
server_thread.daemon = True
server_thread.start()

time.sleep(1)  # Дать серверу время на запуск

# Подключиться к серверу
client_socket = server.connect_to_server("localhost", 9000)

# Отправить сообщение
server.send_message(client_socket, {
    "type": "data",
    "payload": {"key": "value"}
})

# Остановить сервер
server.stop_server()
```

## Конфигурация

### Переменные окружения

Вы можете использовать переменные окружения для конфигурации:

```bash
export LOW_CODE_API_TOKEN="your_api_token"
export LOW_CODE_API_BASE_URL="https://api.example.com"
```

```python
import os
from my_sdk import Client

client = Client(
    token=os.getenv("LOW_CODE_API_TOKEN"),
    base_url=os.getenv("LOW_CODE_API_BASE_URL", "https://api.lowcodeapi.ru")
)
```

### Настройка таймаутов и повторных попыток

```python
from my_sdk.network import NetworkManager

# Кастомные настройки сети
manager = NetworkManager(
    base_url="https://api.example.com",
    timeout=60,  # 60 секунд
    max_retries=5  # 5 попыток
)
```

## Поддержка и обратная связь

Если у вас есть вопросы или предложения по улучшению SDK, пожалуйста:

1. Создайте issue в репозитории GitHub
2. Отправьте email на support@lowcodeapi.ru
3. Посетите нашу документацию: https://docs.lowcodeapi.ru

## Лицензия

Этот SDK распространяется под лицензией MIT. Подробности см. в файле LICENSE.