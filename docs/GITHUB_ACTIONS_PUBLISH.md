# Публикация пакета в PyPI с использованием GitHub Actions

## Требования для настройки автоматической публикации

Для настройки автоматической публикации пакета в PyPI с использованием GitHub Actions необходимо указать следующую информацию:

### Обязательные параметры

1. **Название проекта PyPI (обязательно)**
   - Имя проекта, которое будет создано на PyPI при использовании этого издателя
   - В нашем случае: `low_code_api_lib_sdk`

2. **Владелец (обязательно)**
   - Имя организации GitHub или имя пользователя GitHub, которому принадлежит репозиторий
   - Укажите ваше имя пользователя GitHub или название организации

3. **Имя хранилища (обязательно)**
   - Имя репозитория GitHub, содержащего рабочий процесс публикации
   - Например: `low-code-api-lib-sdk`

4. **Название рабочего процесса (обязательно)**
   - Имя файла издательского процесса
   - Этот файл должен существовать в `.github/workflows/` каталоге в репозитории
   - Например: `publish-to-pypi.yml`

### Опциональные параметры

5. **Название среды (опционально)**
   - Название среды GitHub Actions, которая используется для публикации
   - Должно быть настроено в настройках репозитория
   - Хотя это не обязательно, настоятельно рекомендуется использовать выделенную среду для публикации, особенно если в вашем репозитории есть участники с доступом к коммитам, которые не должны иметь доступ к публикации в PyPI

## Пример файла рабочего процесса GitHub Actions

Создайте файл `.github/workflows/publish-to-pypi.yml` со следующим содержимым:

```yaml
name: Publish Python Package

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: release
    permissions:
      id-token: write  # ВАЖНО для доверенной публикации
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    
    - name: Build package
      run: python -m build
    
    - name: Publish package
      uses: pypa/gh-action-pypi-publish@release/v1
```

## Настройка среды в GitHub

1. Перейдите в настройки вашего репозитория на GitHub
2. Выберите "Environments" в боковом меню
3. Нажмите "New environment"
4. Назовите среду "release"
5. Настройте правила защиты (например, требуемые рецензенты)
6. Сохраните настройки

## Процесс публикации

1. Создайте новый релиз в вашем репозитории GitHub
2. GitHub Actions автоматически запустит рабочий процесс публикации
3. Пакет будет собран и опубликован в PyPI

## Поддержка OpenID Connect

GitHub Actions поддерживает OpenID Connect для безопасной аутентификации в PyPI без необходимости хранить токены API. Это рекомендуемый способ настройки публикации.

Подробнее о поддержке OpenID Connect в GitHub Actions можно узнать в [официальной документации GitHub](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-cloud-providers).