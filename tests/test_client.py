"""Тесты для клиента SDK."""

import unittest
from unittest.mock import Mock, patch
import sys
import os

# Добавляем путь к модулю SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from my_sdk.client import Client
from my_sdk.exceptions import ValidationError
from my_sdk.auth import AuthAPI
from my_sdk.user import UserAPI
from my_sdk.bots import BotsAPI


class TestClient(unittest.TestCase):
    """Тесты для класса Client."""
    
    def setUp(self):
        """Настройка тестов."""
        self.token = "test_token"
        self.base_url = "https://api.example.com"
        self.client = Client(token=self.token, base_url=self.base_url)
    
    def test_init_with_token_only(self):
        """Тест инициализации только с токеном."""
        client = Client(token=self.token)
        self.assertEqual(client.token, self.token)
        self.assertEqual(client.base_url, "https://api.lowcodeapilib.com")
    
    def test_init_with_token_and_base_url(self):
        """Тест инициализации с токеном и базовым URL."""
        self.assertEqual(self.client.token, self.token)
        self.assertEqual(self.client.base_url, self.base_url)
    
    def test_init_without_token(self):
        """Тест инициализации без токена."""
        with self.assertRaises(ValidationError):
            Client(token="")
    
    def test_init_with_invalid_base_url(self):
        """Тест инициализации с невалидным базовым URL."""
        with self.assertRaises(ValidationError):
            Client(token=self.token, base_url="invalid_url")
    
    def test_auth_module_creation(self):
        """Тест создания модуля аутентификации."""
        auth = self.client.auth()
        self.assertIsInstance(auth, AuthAPI)
        self.assertEqual(auth.base_url, self.base_url)
        self.assertEqual(auth.token, self.token)
    
    def test_user_module_creation(self):
        """Тест создания модуля пользователя."""
        user = self.client.user()
        self.assertIsInstance(user, UserAPI)
        self.assertEqual(user.base_url, self.base_url)
        self.assertEqual(user.token, self.token)
    
    def test_bots_module_creation(self):
        """Тест создания модуля ботов."""
        bots = self.client.bots()
        self.assertIsInstance(bots, BotsAPI)
        self.assertEqual(bots.base_url, self.base_url)
        self.assertEqual(bots.token, self.token)
    
    def test_templates_module_creation(self):
        """Тест создания модуля шаблонов."""
        templates = self.client.templates()
        self.assertEqual(templates.base_url, self.base_url)
        self.assertEqual(templates.token, self.token)
    
    def test_media_module_creation(self):
        """Тест создания модуля медиа."""
        media = self.client.media()
        self.assertEqual(media.base_url, self.base_url)
        self.assertEqual(media.token, self.token)
    
    def test_visual_editor_module_creation(self):
        """Тест создания модуля визуального редактора."""
        visual_editor = self.client.visual_editor()
        self.assertEqual(visual_editor.base_url, self.base_url)
        self.assertEqual(visual_editor.token, self.token)
    
    def test_admin_module_creation(self):
        """Тест создания модуля администратора."""
        admin = self.client.admin()
        self.assertEqual(admin.base_url, self.base_url)
        self.assertEqual(admin.token, self.token)
    
    def test_system_module_creation(self):
        """Тест создания модуля системы."""
        system = self.client.system()
        self.assertEqual(system.base_url, self.base_url)
        self.assertEqual(system.token, self.token)
    
    def test_multiple_module_instances(self):
        """Тест создания нескольких экземпляров модулей."""
        auth1 = self.client.auth()
        auth2 = self.client.auth()
        
        # Должны быть разными объектами
        self.assertIsNot(auth1, auth2)
        
        # Но с одинаковыми параметрами
        self.assertEqual(auth1.base_url, auth2.base_url)
        self.assertEqual(auth1.token, auth2.token)
    
    def test_client_string_representation(self):
        """Тест строкового представления клиента."""
        client_str = str(self.client)
        self.assertIn("Client", client_str)
        self.assertIn(self.base_url, client_str)
        # Токен не должен отображаться в строковом представлении
        self.assertNotIn(self.token, client_str)


if __name__ == '__main__':
    unittest.main()