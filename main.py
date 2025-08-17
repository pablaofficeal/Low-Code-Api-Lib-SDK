from my_sdk import Client

def main():
    # Создание клиента с токеном авторизации
    client = Client(token="ваш_токен_авторизации")
    
    # Пример использования модуля аутентификации
    auth = client.auth()
    login_result = auth.login(username="test_user", password="test_password")
    print("Login result:", login_result)
    
    # Пример использования модуля пользователя
    user = client.user()
    user_info = user.get_info()
    print("User info:", user_info)
    
    # Пример использования модуля ботов
    bots = client.bots()
    bot_status = bots.get_bot_status(bot_id=123)
    print("Bot status:", bot_status)
    
    # Пример использования модуля системы
    system = client.system()
    health_check = system.health_check()
    print("Health check:", health_check)

if __name__ == "__main__":
    main()