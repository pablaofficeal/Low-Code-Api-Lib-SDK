# Примеры использования - Low Code API Lib SDK v0.1.1

Этот документ содержит практические примеры использования Low Code API Lib SDK.

## Содержание

- [Быстрый старт](#быстрый-старт)
- [Работа с пользователями](#работа-с-пользователями)
- [Работа с ботами](#работа-с-ботами)
- [Загрузка и скачивание файлов](#загрузка-и-скачивание-файлов)
- [Отправка сообщений](#отправка-сообщений)
- [Настройка вебхуков](#настройка-вебхуков)
- [Обработка ошибок](#обработка-ошибок)
- [Сетевое взаимодействие](#сетевое-взаимодействие)
- [Продвинутые примеры](#продвинутые-примеры)

## Быстрый старт

### Установка и базовая настройка

```python
# Установка SDK
# pip install low-code-api-lib-sdk

from my_sdk import Client
from my_sdk.exceptions import SDKError

# Инициализация клиента
client = Client(
    token="your_api_token_here",
    base_url="https://api.lowcodeapi.ru"  # опционально
)

# Проверка подключения
try:
    user_info = client.auth.get_me()
    print(f"Успешно подключен как: {user_info['name']}")
except SDKError as e:
    print(f"Ошибка подключения: {e}")
```

### Использование переменных окружения

```python
import os
from my_sdk import Client

# Установите переменные окружения:
# export LOW_CODE_API_TOKEN="your_token"
# export LOW_CODE_API_BASE_URL="https://api.example.com"

client = Client(
    token=os.getenv("LOW_CODE_API_TOKEN"),
    base_url=os.getenv("LOW_CODE_API_BASE_URL")
)
```

## Работа с пользователями

### Получение списка пользователей

```python
from my_sdk import Client
from my_sdk.exceptions import ValidationError, NetworkError

client = Client(token="your_token")

try:
    # Получить всех пользователей
    users = client.users.get_users()
    print(f"Найдено пользователей: {len(users)}")
    
    for user in users:
        print(f"ID: {user['id']}, Имя: {user['name']}, Email: {user['email']}")
        
except NetworkError as e:
    print(f"Сетевая ошибка: {e}")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
```

### Создание нового пользователя

```python
def create_user_example():
    client = Client(token="your_token")
    
    user_data = {
        "name": "Иван Петров",
        "email": "ivan.petrov@example.com",
        "phone": "+7 (999) 123-45-67",
        "role": "user"
    }
    
    try:
        new_user = client.users.create_user(user_data)
        print(f"Пользователь создан успешно:")
        print(f"ID: {new_user['id']}")
        print(f"Имя: {new_user['name']}")
        print(f"Email: {new_user['email']}")
        return new_user
        
    except ValidationError as e:
        print(f"Ошибка валидации данных: {e}")
        return None
    except Exception as e:
        print(f"Ошибка создания пользователя: {e}")
        return None

# Использование
new_user = create_user_example()
```

### Обновление пользователя

```python
def update_user_example(user_id):
    client = Client(token="your_token")
    
    # Данные для обновления
    update_data = {
        "name": "Иван Петрович Петров",
        "phone": "+7 (999) 987-65-43"
    }
    
    try:
        updated_user = client.users.update_user(user_id, update_data)
        print(f"Пользователь обновлен: {updated_user['name']}")
        return updated_user
        
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")
    except Exception as e:
        print(f"Ошибка обновления: {e}")
    
    return None
```

### Поиск пользователя

```python
def find_user_by_email(email):
    client = Client(token="your_token")
    
    try:
        users = client.users.get_users()
        
        for user in users:
            if user.get('email') == email:
                print(f"Пользователь найден: {user['name']} ({user['id']})")
                return user
        
        print(f"Пользователь с email {email} не найден")
        return None
        
    except Exception as e:
        print(f"Ошибка поиска: {e}")
        return None

# Использование
user = find_user_by_email("ivan.petrov@example.com")
```

## Работа с ботами

### Создание и настройка бота

```python
def create_bot_example():
    client = Client(token="your_token")
    
    bot_config = {
        "name": "Помощник поддержки",
        "description": "Бот для автоматической поддержки пользователей",
        "settings": {
            "auto_reply": True,
            "working_hours": "9:00-18:00",
            "language": "ru"
        }
    }
    
    try:
        new_bot = client.bots.create_bot(bot_config)
        print(f"Бот создан: {new_bot['name']} (ID: {new_bot['id']})")
        
        # Настройка дополнительных параметров
        bot_id = new_bot['id']
        additional_settings = {
            "welcome_message": "Привет! Я ваш виртуальный помощник.",
            "fallback_message": "Извините, я не понял ваш вопрос. Обратитесь к оператору."
        }
        
        updated_bot = client.bots.update_bot(bot_id, additional_settings)
        print(f"Бот настроен: {updated_bot['name']}")
        
        return updated_bot
        
    except Exception as e:
        print(f"Ошибка создания бота: {e}")
        return None

# Использование
bot = create_bot_example()
```

### Управление ботами

```python
def manage_bots_example():
    client = Client(token="your_token")
    
    try:
        # Получить список всех ботов
        bots = client.bots.get_bots()
        print(f"Всего ботов: {len(bots)}")
        
        for bot in bots:
            print(f"Бот: {bot['name']} (ID: {bot['id']})")
            print(f"Статус: {bot.get('status', 'unknown')}")
            print(f"Описание: {bot.get('description', 'Нет описания')}")
            print("-" * 40)
            
            # Получить детальную информацию о боте
            bot_details = client.bots.get_bot(bot['id'])
            print(f"Детали бота {bot['name']}:")
            print(f"Создан: {bot_details.get('created_at')}")
            print(f"Настройки: {bot_details.get('settings')}")
            print("=" * 40)
            
    except Exception as e:
        print(f"Ошибка получения ботов: {e}")

# Использование
manage_bots_example()
```

## Загрузка и скачивание файлов

### Загрузка файла

```python
def upload_file_example(file_path):
    client = Client(token="your_token")
    
    try:
        with open(file_path, "rb") as file:
            # Загрузка файла
            uploaded_file = client.files.upload_file(file)
            
            print(f"Файл загружен успешно:")
            print(f"ID: {uploaded_file['id']}")
            print(f"Имя: {uploaded_file['filename']}")
            print(f"Размер: {uploaded_file['size']} байт")
            print(f"URL: {uploaded_file.get('url')}")
            
            return uploaded_file
            
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
    except Exception as e:
        print(f"Ошибка загрузки файла: {e}")
    
    return None

# Использование
uploaded = upload_file_example("document.pdf")
```

### Скачивание файла

```python
def download_file_example(file_id, save_path):
    client = Client(token="your_token")
    
    try:
        # Получить информацию о файле
        file_info = client.files.get_file(file_id)
        print(f"Скачивание файла: {file_info['filename']}")
        
        # Скачать содержимое файла
        file_content = client.files.download_file(file_id)
        
        # Сохранить файл
        with open(save_path, "wb") as file:
            file.write(file_content)
        
        print(f"Файл сохранен: {save_path}")
        return True
        
    except Exception as e:
        print(f"Ошибка скачивания файла: {e}")
        return False

# Использование
success = download_file_example("file_id_123", "downloaded_document.pdf")
```

### Массовая загрузка файлов

```python
import os
from pathlib import Path

def bulk_upload_files(directory_path):
    client = Client(token="your_token")
    uploaded_files = []
    
    try:
        directory = Path(directory_path)
        
        for file_path in directory.iterdir():
            if file_path.is_file():
                print(f"Загружаем: {file_path.name}")
                
                try:
                    with open(file_path, "rb") as file:
                        uploaded_file = client.files.upload_file(file)
                        uploaded_files.append(uploaded_file)
                        print(f"✓ Загружен: {uploaded_file['filename']}")
                        
                except Exception as e:
                    print(f"✗ Ошибка загрузки {file_path.name}: {e}")
        
        print(f"\nВсего загружено файлов: {len(uploaded_files)}")
        return uploaded_files
        
    except Exception as e:
        print(f"Ошибка массовой загрузки: {e}")
        return []

# Использование
uploaded_files = bulk_upload_files("./documents")
```

## Отправка сообщений

### Простая отправка сообщения

```python
def send_simple_message(recipient_id, text):
    client = Client(token="your_token")
    
    message_data = {
        "recipient_id": recipient_id,
        "text": text,
        "type": "text"
    }
    
    try:
        sent_message = client.messages.send_message(message_data)
        print(f"Сообщение отправлено: {sent_message['id']}")
        return sent_message
        
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")
        return None

# Использование
message = send_simple_message("user_123", "Привет! Как дела?")
```

### Отправка сообщения с вложениями

```python
def send_message_with_attachment(recipient_id, text, file_path):
    client = Client(token="your_token")
    
    try:
        # Сначала загружаем файл
        with open(file_path, "rb") as file:
            uploaded_file = client.files.upload_file(file)
        
        # Затем отправляем сообщение с вложением
        message_data = {
            "recipient_id": recipient_id,
            "text": text,
            "attachments": [{
                "type": "file",
                "file_id": uploaded_file['id']
            }]
        }
        
        sent_message = client.messages.send_message(message_data)
        print(f"Сообщение с вложением отправлено: {sent_message['id']}")
        return sent_message
        
    except Exception as e:
        print(f"Ошибка отправки сообщения с вложением: {e}")
        return None

# Использование
message = send_message_with_attachment(
    "user_123", 
    "Отправляю вам документ", 
    "contract.pdf"
)
```

### Массовая рассылка

```python
def send_bulk_messages(recipient_ids, text):
    client = Client(token="your_token")
    sent_messages = []
    failed_sends = []
    
    for recipient_id in recipient_ids:
        try:
            message_data = {
                "recipient_id": recipient_id,
                "text": text,
                "type": "text"
            }
            
            sent_message = client.messages.send_message(message_data)
            sent_messages.append(sent_message)
            print(f"✓ Отправлено пользователю {recipient_id}")
            
        except Exception as e:
            failed_sends.append({"recipient_id": recipient_id, "error": str(e)})
            print(f"✗ Ошибка отправки пользователю {recipient_id}: {e}")
    
    print(f"\nРезультат рассылки:")
    print(f"Успешно отправлено: {len(sent_messages)}")
    print(f"Ошибок: {len(failed_sends)}")
    
    return sent_messages, failed_sends

# Использование
recipients = ["user_1", "user_2", "user_3"]
sent, failed = send_bulk_messages(recipients, "Важное уведомление!")
```

## Настройка вебхуков

### Создание вебхука

```python
def setup_webhook_example():
    client = Client(token="your_token")
    
    webhook_config = {
        "url": "https://myapp.com/webhook/handler",
        "events": [
            "user.created",
            "user.updated",
            "message.sent",
            "message.received",
            "bot.message"
        ],
        "secret": "my_webhook_secret_key",
        "active": True
    }
    
    try:
        webhook = client.webhooks.create_webhook(webhook_config)
        print(f"Вебхук создан: {webhook['id']}")
        print(f"URL: {webhook['url']}")
        print(f"События: {', '.join(webhook['events'])}")
        return webhook
        
    except Exception as e:
        print(f"Ошибка создания вебхука: {e}")
        return None

# Использование
webhook = setup_webhook_example()
```

### Обработчик вебхука (Flask пример)

```python
from flask import Flask, request, jsonify
import hashlib
import hmac

app = Flask(__name__)
WEBHOOK_SECRET = "my_webhook_secret_key"

def verify_webhook_signature(payload, signature, secret):
    """Проверка подписи вебхука"""
    expected_signature = hmac.new(
        secret.encode('utf-8'),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(f"sha256={expected_signature}", signature)

@app.route('/webhook/handler', methods=['POST'])
def webhook_handler():
    # Получаем данные
    payload = request.get_data()
    signature = request.headers.get('X-Signature-256')
    
    # Проверяем подпись
    if not verify_webhook_signature(payload, signature, WEBHOOK_SECRET):
        return jsonify({"error": "Invalid signature"}), 401
    
    # Обрабатываем событие
    event_data = request.get_json()
    event_type = event_data.get('event')
    
    if event_type == 'user.created':
        handle_user_created(event_data['data'])
    elif event_type == 'message.sent':
        handle_message_sent(event_data['data'])
    elif event_type == 'bot.message':
        handle_bot_message(event_data['data'])
    
    return jsonify({"status": "ok"})

def handle_user_created(user_data):
    print(f"Новый пользователь: {user_data['name']} ({user_data['email']})")
    # Ваша логика обработки

def handle_message_sent(message_data):
    print(f"Отправлено сообщение: {message_data['text']}")
    # Ваша логика обработки

def handle_bot_message(message_data):
    print(f"Сообщение от бота: {message_data['text']}")
    # Ваша логика обработки

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

## Обработка ошибок

### Комплексная обработка ошибок

```python
from my_sdk import Client
from my_sdk.exceptions import (
    SDKError, AuthenticationError, NetworkError, 
    ValidationError, TimeoutError, RateLimitError, ServerError
)
import time
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def robust_api_call(client, operation, *args, **kwargs):
    """Надежный вызов API с обработкой ошибок и повторными попытками"""
    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            result = operation(*args, **kwargs)
            logger.info(f"Операция выполнена успешно с {attempt + 1} попытки")
            return result
            
        except AuthenticationError as e:
            logger.error(f"Ошибка аутентификации: {e}")
            # Не повторяем при ошибках аутентификации
            raise
            
        except ValidationError as e:
            logger.error(f"Ошибка валидации: {e}")
            # Не повторяем при ошибках валидации
            raise
            
        except RateLimitError as e:
            logger.warning(f"Превышен лимит запросов: {e}")
            if attempt < max_retries - 1:
                # Увеличиваем задержку при превышении лимита
                delay = retry_delay * (2 ** attempt) * 5
                logger.info(f"Ожидание {delay} секунд перед повтором...")
                time.sleep(delay)
                continue
            raise
            
        except (NetworkError, TimeoutError) as e:
            logger.warning(f"Сетевая ошибка (попытка {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                delay = retry_delay * (2 ** attempt)
                logger.info(f"Повтор через {delay} секунд...")
                time.sleep(delay)
                continue
            raise
            
        except ServerError as e:
            logger.error(f"Серверная ошибка: {e}")
            if attempt < max_retries - 1:
                delay = retry_delay * (2 ** attempt)
                logger.info(f"Повтор через {delay} секунд...")
                time.sleep(delay)
                continue
            raise
            
        except SDKError as e:
            logger.error(f"Общая ошибка SDK: {e}")
            raise
            
        except Exception as e:
            logger.error(f"Неожиданная ошибка: {e}")
            raise
    
    raise Exception(f"Операция не удалась после {max_retries} попыток")

# Пример использования
def safe_get_users():
    client = Client(token="your_token")
    
    try:
        users = robust_api_call(client, client.users.get_users)
        return users
    except Exception as e:
        logger.error(f"Не удалось получить пользователей: {e}")
        return []

# Использование
users = safe_get_users()
print(f"Получено пользователей: {len(users)}")
```

## Сетевое взаимодействие

### Создание сетевого сервера

```python
from my_sdk.network import NetworkSharing
import threading
import json
import time

def create_data_server():
    """Создание сервера для обмена данными"""
    server = NetworkSharing(host="localhost", port=9000)
    
    def handle_client_message(client_socket, message):
        """Обработка сообщений от клиентов"""
        print(f"Получено сообщение: {message}")
        
        if message.get('type') == 'get_data':
            # Отправляем данные клиенту
            response = {
                'type': 'data_response',
                'data': {
                    'timestamp': time.time(),
                    'server_status': 'active',
                    'clients_count': len(server.clients)
                }
            }
            server.send_to_client(client_socket, response)
            
        elif message.get('type') == 'broadcast_request':
            # Широковещательная отправка
            broadcast_message = {
                'type': 'broadcast',
                'data': message.get('data'),
                'from': 'server'
            }
            server.broadcast_message(broadcast_message)
    
    # Переопределяем обработчик сообщений
    server.handle_client_message = handle_client_message
    
    # Запускаем сервер в отдельном потоке
    server_thread = threading.Thread(target=server.start_server)
    server_thread.daemon = True
    server_thread.start()
    
    print("Сервер запущен на localhost:9000")
    return server

# Использование
server = create_data_server()
```

### Клиент для подключения к серверу

```python
from my_sdk.network import NetworkSharing
import json
import time

def create_data_client():
    """Создание клиента для подключения к серверу"""
    client_sharing = NetworkSharing()
    
    try:
        # Подключаемся к серверу
        client_socket = client_sharing.connect_to_server("localhost", 9000)
        print("Подключен к серверу")
        
        # Запрашиваем данные
        request_message = {
            'type': 'get_data',
            'client_id': 'client_001'
        }
        client_sharing.send_message(client_socket, request_message)
        
        # Отправляем запрос на широковещательную рассылку
        time.sleep(1)
        broadcast_request = {
            'type': 'broadcast_request',
            'data': 'Привет всем от клиента!'
        }
        client_sharing.send_message(client_socket, broadcast_request)
        
        return client_socket
        
    except Exception as e:
        print(f"Ошибка подключения клиента: {e}")
        return None

# Использование
client_socket = create_data_client()
```

## Продвинутые примеры

### Система уведомлений

```python
from my_sdk import Client
from my_sdk.exceptions import SDKError
import asyncio
import json
from datetime import datetime, timedelta

class NotificationSystem:
    def __init__(self, token):
        self.client = Client(token=token)
        self.notification_queue = []
    
    def add_notification(self, recipient_id, message, send_at=None, priority="normal"):
        """Добавить уведомление в очередь"""
        notification = {
            'id': len(self.notification_queue) + 1,
            'recipient_id': recipient_id,
            'message': message,
            'send_at': send_at or datetime.now(),
            'priority': priority,
            'status': 'pending'
        }
        self.notification_queue.append(notification)
        return notification['id']
    
    def send_immediate_notification(self, recipient_id, message):
        """Отправить уведомление немедленно"""
        try:
            message_data = {
                'recipient_id': recipient_id,
                'text': message,
                'type': 'notification'
            }
            
            result = self.client.messages.send_message(message_data)
            print(f"Уведомление отправлено: {result['id']}")
            return result
            
        except SDKError as e:
            print(f"Ошибка отправки уведомления: {e}")
            return None
    
    def process_notification_queue(self):
        """Обработать очередь уведомлений"""
        current_time = datetime.now()
        
        for notification in self.notification_queue:
            if (notification['status'] == 'pending' and 
                notification['send_at'] <= current_time):
                
                try:
                    self.send_immediate_notification(
                        notification['recipient_id'],
                        notification['message']
                    )
                    notification['status'] = 'sent'
                    notification['sent_at'] = current_time
                    
                except Exception as e:
                    notification['status'] = 'failed'
                    notification['error'] = str(e)
                    print(f"Ошибка отправки уведомления {notification['id']}: {e}")
    
    def schedule_daily_reminder(self, recipient_id, message, hour=9, minute=0):
        """Запланировать ежедневное напоминание"""
        tomorrow = datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
        if tomorrow <= datetime.now():
            tomorrow += timedelta(days=1)
        
        return self.add_notification(recipient_id, message, tomorrow, "high")
    
    def get_notification_stats(self):
        """Получить статистику уведомлений"""
        stats = {
            'total': len(self.notification_queue),
            'pending': 0,
            'sent': 0,
            'failed': 0
        }
        
        for notification in self.notification_queue:
            stats[notification['status']] += 1
        
        return stats

# Пример использования
notification_system = NotificationSystem("your_token")

# Немедленное уведомление
notification_system.send_immediate_notification(
    "user_123", 
    "Важное уведомление: ваш заказ готов!"
)

# Отложенное уведомление
future_time = datetime.now() + timedelta(hours=2)
notification_system.add_notification(
    "user_456",
    "Напоминание: встреча через 30 минут",
    future_time
)

# Ежедневное напоминание
notification_system.schedule_daily_reminder(
    "user_789",
    "Доброе утро! Не забудьте проверить задачи на сегодня"
)

# Обработка очереди
notification_system.process_notification_queue()

# Статистика
stats = notification_system.get_notification_stats()
print(f"Статистика уведомлений: {stats}")
```

### Система мониторинга API

```python
from my_sdk import Client
from my_sdk.network import get_network_manager
import time
import json
from datetime import datetime

class APIMonitor:
    def __init__(self, token, base_url=None):
        self.client = Client(token=token, base_url=base_url)
        self.network_manager = get_network_manager(base_url or "https://api.lowcodeapi.ru")
        self.metrics = {
            'requests_count': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'average_response_time': 0,
            'response_times': [],
            'errors': []
        }
    
    def monitor_endpoint(self, method, endpoint, **kwargs):
        """Мониторинг конкретного эндпоинта"""
        start_time = time.time()
        
        try:
            if method.upper() == 'GET':
                response = self.network_manager.get(endpoint, **kwargs)
            elif method.upper() == 'POST':
                response = self.network_manager.post(endpoint, **kwargs)
            elif method.upper() == 'PUT':
                response = self.network_manager.put(endpoint, **kwargs)
            elif method.upper() == 'DELETE':
                response = self.network_manager.delete(endpoint, **kwargs)
            else:
                response = self.network_manager.request(method, endpoint, **kwargs)
            
            end_time = time.time()
            response_time = end_time - start_time
            
            # Обновляем метрики
            self.metrics['requests_count'] += 1
            self.metrics['successful_requests'] += 1
            self.metrics['response_times'].append(response_time)
            
            # Пересчитываем среднее время ответа
            self.metrics['average_response_time'] = sum(self.metrics['response_times']) / len(self.metrics['response_times'])
            
            print(f"✓ {method} {endpoint} - {response.status_code} ({response_time:.3f}s)")
            return response
            
        except Exception as e:
            end_time = time.time()
            response_time = end_time - start_time
            
            # Обновляем метрики ошибок
            self.metrics['requests_count'] += 1
            self.metrics['failed_requests'] += 1
            self.metrics['errors'].append({
                'timestamp': datetime.now().isoformat(),
                'method': method,
                'endpoint': endpoint,
                'error': str(e),
                'response_time': response_time
            })
            
            print(f"✗ {method} {endpoint} - Error: {e} ({response_time:.3f}s)")
            raise
    
    def health_check(self):
        """Проверка здоровья API"""
        endpoints_to_check = [
            ('GET', '/auth/me'),
            ('GET', '/users'),
            ('GET', '/bots')
        ]
        
        health_status = {
            'timestamp': datetime.now().isoformat(),
            'status': 'healthy',
            'checks': []
        }
        
        for method, endpoint in endpoints_to_check:
            try:
                start_time = time.time()
                response = self.monitor_endpoint(method, endpoint)
                end_time = time.time()
                
                check_result = {
                    'endpoint': f"{method} {endpoint}",
                    'status': 'ok',
                    'response_time': end_time - start_time,
                    'status_code': response.status_code
                }
                
            except Exception as e:
                check_result = {
                    'endpoint': f"{method} {endpoint}",
                    'status': 'error',
                    'error': str(e)
                }
                health_status['status'] = 'unhealthy'
            
            health_status['checks'].append(check_result)
        
        return health_status
    
    def get_metrics_report(self):
        """Получить отчет по метрикам"""
        if self.metrics['requests_count'] == 0:
            return "Нет данных для отчета"
        
        success_rate = (self.metrics['successful_requests'] / self.metrics['requests_count']) * 100
        
        report = f"""
=== Отчет по мониторингу API ===
Всего запросов: {self.metrics['requests_count']}
Успешных: {self.metrics['successful_requests']}
Ошибок: {self.metrics['failed_requests']}
Процент успеха: {success_rate:.2f}%
Среднее время ответа: {self.metrics['average_response_time']:.3f}s

Последние ошибки:
"""
        
        for error in self.metrics['errors'][-5:]:  # Последние 5 ошибок
            report += f"- {error['timestamp']}: {error['method']} {error['endpoint']} - {error['error']}\n"
        
        return report

# Пример использования
monitor = APIMonitor("your_token")

# Проверка здоровья
health = monitor.health_check()
print(json.dumps(health, indent=2, ensure_ascii=False))

# Мониторинг конкретных запросов
try:
    users = monitor.monitor_endpoint('GET', '/users')
    print(f"Получено пользователей: {len(users.json())}")
except Exception as e:
    print(f"Ошибка получения пользователей: {e}")

# Отчет по метрикам
print(monitor.get_metrics_report())
```

Эти примеры демонстрируют различные способы использования Low Code API Lib SDK для решения реальных задач. Вы можете адаптировать их под свои потребности и расширять функциональность по мере необходимости.