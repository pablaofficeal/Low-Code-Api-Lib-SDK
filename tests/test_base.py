"""Тесты для базовой функциональности SDK."""

import unittest
from unittest.mock import Mock, patch
import sys
import os

# Добавляем путь к модулю SDK
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from my_sdk.base import BaseAPI
from my_sdk.exceptions import ValidationError, AuthenticationError


class TestBaseAPI(unittest.TestCase):
    """Тесты для класса BaseAPI."""
    
    def setUp(self):
        """Настройка тестов."""
        self.base_url = "https://api.example.com"
        self.token = "test_token"
        self.api = BaseAPI(self.base_url, self.token)
    
    def test_init_with_valid_params(self):
        """Тест инициализации с валидными параметрами."""
        self.assertEqual(self.api.base_url, self.base_url)
        self.assertEqual(self.api.token, self.token)
        self.assertIsNotNone(self.api.session)
    
    def test_init_without_token(self):
        """Тест инициализации без токена."""
        with self.assertRaises(ValidationError):
            BaseAPI(self.base_url, "")
    
    def test_init_without_base_url(self):
        """Тест инициализации без базового URL."""
        with self.assertRaises(ValidationError):
            BaseAPI("", self.token)
    
    def test_init_with_invalid_url(self):
        """Тест инициализации с невалидным URL."""
        with self.assertRaises(ValidationError):
            BaseAPI("invalid_url", self.token)
    
    @patch('requests.Session.request')
    def test_make_request_success(self, mock_request):
        """Тест успешного выполнения запроса."""
        # Настройка мока
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = {"status": "success"}
        mock_request.return_value = mock_response
        
        # Выполнение запроса
        result = self.api._make_request('GET', '/test')
        
        # Проверки
        self.assertEqual(result, {"status": "success"})
        mock_request.assert_called_once()
    
    @patch('requests.Session.request')
    def test_make_request_with_auth_error(self, mock_request):
        """Тест запроса с ошибкой аутентификации."""
        # Настройка мока для ошибки 401
        mock_response = Mock()
        mock_response.ok = False
        mock_response.status_code = 401
        mock_response.json.return_value = {"message": "Unauthorized"}
        mock_request.return_value = mock_response
        
        # Проверка, что выбрасывается исключение
        with self.assertRaises(AuthenticationError):
            self.api._make_request('GET', '/test')
    
    def test_headers_contain_authorization(self):
        """Тест наличия заголовка авторизации."""
        headers = self.api._get_headers()
        self.assertIn('Authorization', headers)
        self.assertEqual(headers['Authorization'], f'Bearer {self.token}')
    
    def test_headers_contain_content_type(self):
        """Тест наличия заголовка Content-Type."""
        headers = self.api._get_headers()
        self.assertIn('Content-Type', headers)
        self.assertEqual(headers['Content-Type'], 'application/json')


if __name__ == '__main__':
    unittest.main()