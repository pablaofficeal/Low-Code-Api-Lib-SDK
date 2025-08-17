from my_sdk import Client

def main():
    # Создание клиента с токеном авторизации
    print("Инициализация клиента SDK...")
    client = Client(token="test_token")
    print("Клиент SDK успешно инициализирован!")
    
    # Демонстрация доступа к модулям (без выполнения реальных запросов)
    print("\nДоступные модули SDK:")
    
    # Модуль аутентификации
    auth = client.auth()
    print("- Auth модуль доступен")
    
    # Модуль пользователя
    user = client.user()
    print("- User модуль доступен")
    
    # Модуль ботов
    bots = client.bots()
    print("- Bots модуль доступен")
    
    # Модуль шаблонов
    templates = client.templates()
    print("- Templates модуль доступен")
    
    # Модуль медиа
    media = client.media()
    print("- Media модуль доступен")
    
    # Модуль визуального редактора
    visual_editor = client.visual_editor()
    print("- VisualEditor модуль доступен")
    
    # Модуль администратора
    admin = client.admin()
    print("- Admin модуль доступен")
    
    # Модуль системы
    system = client.system()
    print("- System модуль доступен")
    
    print("\nSDK успешно протестирован!")
    print("Для выполнения реальных запросов необходимо указать правильный base_url и токен авторизации.")

if __name__ == "__main__":
    main()