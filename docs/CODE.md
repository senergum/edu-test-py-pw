# ПРАВИЛА НАПИСАНИЯ КОДА
* Тут собранны рекомендации которые желательно соблюдать
* [Инструкция написания и эксплуатации авто-тестов на `Python`](https://disk.yandex.ru/i/p6A-v9AiGy5qxA)

## Структура проекта
* Далее будет общее описание принципов написания авто-тестов и кода в частности
### `Page Objects` Модель (Она же `POM`)
* Используется Page Objects модель, скрипты взаимодействия со страницей хранятся в /page, тесты — в /tests.
* Тут речь идёт про Page Objects модели в папке /page, в которых локаторы и тестовые данные разделены:
* Плохо: локаторы в тестах
```
page.locator("#login").click()
```
* Хорошо: вынесено в отдельный файл, например login_locators.py
```
# импорт
from page.modulename.modulename_locators import *

page.locator(BUTTON).click()
```
* Аналогично с данными, выносятся в отдельный файл, например login_data.py

### Правило AAA (`Arrange` `Act` `Assert`) 
* Прямой перевод: `Организовать` `Сделать` `Проверить`
* Адаптированный: `Аранжировка` `Атака` `Анализ`
* Тут речь идёт про тесты в папке /tests
```
def test_login():
    # Arrange (Организовать)
    page.goto(LOGIN_URL)
    auth_data = {"user": LOGIN, "pass": PASS}
    
    # Act (Сделать)
    login_page.fill_credentials(auth_data)
    login_page.submit()
    
    # Assert (Проверить)
    assert dashboard_page.is_loaded()
```

## Независимость тестов
* Каждый тест должен работать без зависимостей от других тестов.
* Используйте фикстуры для очистки данных:
```
@pytest.fixture
def clean_user_db(api_client):
    yield
    api_client.delete(TEST_USER)
```

## Работа с Page Objects
* Методы Page Object должны возвращать self 
* Это для чейнинга (цепочки) - подход, при котором методы класса возвращают self (т.е. сам объект), что позволяет вызывать их последовательно в одной строке:
```class LoginPage:
    def enter_username(self, username):
        self.page.locator(AUTH_NAME).fill(USER)
        return self  # <- Ключевая строка!
        
    def enter_password(self, password):
        self.page.locator(AUTH_PASS).fill(PASS)
        return self
```
* Пример без цепочки:
```
login_page.enter_username(USER)
login_page.enter_password(PASS)
login_page.click_submit(BUTTON)
```
* Пример с цепочкой:
```
login_page.enter_username(USER).enter_password(PASS).click_submit(BUTTON)
```
* Не добавляйте проверки в Page Objects (это работа тестов).

## Обработка ошибок
* Используйте custom exceptions:
```
class ElementNotFoundError(Exception):
    pass
    
def click_element(locator):
    if not page.locator(locator).is_visible():
        raise ElementNotFoundError(f"Элемент {locator} не найден")
```

## Стиль локаторов
* Плохо:
```
page.locator("//button[@id='login']")  # Избыточный XPath
page.locator(".btn-primary >> nth=3")  # Хрупкий селектор
```
* Хорошо:
```
# В page\login_page\login_locators.py
LOGIN_BTN = "button#login"  # CSS-селектор
SUBMIT_BTN = "data-testid=submit-button"  # Атрибут test-id

# В тесте
page.locator(LOGIN_BTN).click()  
page.locator(SUBMIT_BTN).hover()
```

## Организация импортов
* Плохо:
```
from page.login_page import *
from page.login_page.login_locators import *
from data.locators import LOGIN_BTN, PASSWORD_FIELD  # Хаотичный импорт
```
* Хорошо:
```
# Группировка импортов с пустыми строками между блоками
import pytest
from playwright.sync_api import Page

# Локаторы и данные
from page.login_page.login_locators import *
from page.login_page.login_data import *
# Алиасы лучше не делать, будем придерживаться одного стиля, алиасы выглядят так:
from page.login_page.login_locators import LoginLocators as LL
from page.login_page.login_data import DataLocators as DL

# Page Objects
from page.login_page import LoginPage
from page.module_page import ModulePage
```

## Именования
* Примеры:
```
Переменные                  user_credentials
Классы                      LoginPage
Константы (data)            DEFAULT_TIMEOUT
Тест                        test_modulename.py
Page Object                 modulename_page.py
Фикстуры                    @pytest.fixture \ def chrome_browser()
Тестовый метод              def test_modulename_assert()
```

## Общие правила написания кода
* Стиль кода (PEP 8)
```
# Плохо
def test_login():
    page.locator('button#Login').click()  # Смешение кавычек, нет пробелов

# Хорошо
def test_login():
    page.locator("button#login").click()  # Единый стиль кавычек
```
* Табуляция и отступы:
  * Используйте 4 пробела на уровень отступа
  * Максимальная длина строки 120 символов
* Пробелы вокруг операторов
```
# Плохо
x=1
y = x+2

# Хорошо
x = 1
y = x + 2
```
* Нет пробелов
  * Внутри скобок: func(arg), а не func( arg )
  * Перед запятыми/двоеточиями: {"key": value}
  * Перед : в срезах: array[1:2]
* Есть пробелы:
  * После запятых: func(a, b, c)
  * Вокруг = при аннотациях: def func(param: int = 0)
* Длина строки
  * Максимум 79 символов (желательно), 120 — абсолютный максимум. 
  * Перенос строк через \ или скобки:
```
# Хорошо
result = page.locator(
    "button:has-text('Submit') >> nth=0"
).text_content()

# Или
long_string = (
    "Это очень длинная строка, которая "
    "не помещается в 79 символов"
)
```
* Пустые строки
  * 2 пустые строки между классами/функциями верхнего уровня 
  * 1 пустая строка между методами класса 
  * Пробел между логическими блоками:
```
def test_login():
    # Arrange
    page.goto("/login")
    credentials = {"user": "admin", "pass": "qwerty"}
    
    # Act
    login_page.fill_form(credentials)
    
    # Assert
    assert page.url == "/dashboard"
```
* Переносы в многострочных выражениях
  * Для аргументов:
```
page.locator(
    "button >> nth=0",
    timeout=5000,
).click()
```
* Для словарей:
```
credentials = {
    "username": "test",
    "password": "qwerty123",
}
```
* Как проверять код?
  * В IDE:
    * PyCharm: Ctrl + Alt + L (реформат кода)
    * VS Code: установите расширение Python + flake8
  * Автоматически:
```
flake8 path/to/tests/  # Проверяет PEP 8
pylint path/to/tests/  # Более строгий анализ
```

## Документирование и комментирования
* Комментарии
```
# Плохо:
x = 10  # Set x to 10

# Хорошо:
# Таймаут ожидания элементов (сек)
ELEMENT_TIMEOUT = 10
```
* Тесты: Добавляйте docstring с описанием сценария.
```
def test_login_with_expired_password():
    """
    Проверка блокировки входа при истёкшем пароле.
    Ожидаемый результат: 
      - Появляется ошибка 'Password expired'
    """
```
* Фикстуры: Указывайте scope и назначение:
```
@pytest.fixture(scope="module")
def auth_token():
    """Фикстура возвращает JWT-токен для авторизованных запросов."""
```

## Работа с CI/CD
* Теги для разных запусков:
```
pytest -m "smoke"           # Только smoke-тесты
```
* Параметризация через conftest.py.

## Поддержка мультибраузерности
```
# conftest.py
@pytest.fixture(params=["chromium", "firefox"])
def browser(request):
    with sync_playwright() as p:
        browser = getattr(p, request.param).launch()
        yield browser
```

## Отчёты
```
@allure.step("Заполнение логина и пароля")
def fill_credentials(self, username, password):
    ...
```

## Оптимизация
* Параллельный запуск:
```
pytest -n 4  # 4 потока
```
* Кеширование часто используемых данных (например, токенов).

## Проверка качества кода
* Pylint / Flake8 – линтинг (автоматизированная проверка кода)
* pytest --cov – проверка покрытия кода тестами.
* pre-commit – автоматические проверки перед коммитом.
