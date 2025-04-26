# **Шаблон автоматизированного тестирования** 
* Учебный проект (и шаблон) автоматизации труда ручного тестирования.
* Основной функционал - UI скрипты на `python` с использованием библиотеки `playwright`.
* В качестве примера автоматизируется проект [saucedemo](https://www.saucedemo.com/v1/)
* [Скачать `Python` 13+](https://www.python.org/downloads/)
* [Инструкция установки `Python` глава 2.1, эксплуатация глава 3](https://disk.yandex.ru/edit/d/ziggIjO2lsG0H2023WbIniPegnqahzm72s0qoIz-cKg6UlFmWEZta1prdw)
* [Скачать `PyCharm` Community Edition 2025+](https://www.jetbrains.com/ru-ru/pycharm/download/other.html)
* [Инструкция установки `PyCharm` глава 2.2, эксплуатация глава 4](https://disk.yandex.ru/edit/d/ziggIjO2lsG0H2023WbIniPegnqahzm72s0qoIz-cKg6UlFmWEZta1prdw)
* [Скачать `git`](https://git-scm.com/downloads)
* [Инструкция установки и эксплуатации `git` глава 4.5](https://disk.yandex.ru/i/p6A-v9AiGy5qxA)

## **Требования к запуску**
* Описаны в файле `requirements.txt`
* Установка требований из этого файла:
```
pip install requirements.txt
```
* Альтернативная установка требований:
```
pip install playwright pytest pytest-playwright pytest-html allure-pytest requests locust
```
* После установки пакетов, установите браузера `playwright`, этой командой установятся все 3 (firefox, chromium, webkit) браузера:
```
playwright install
```
* Можно указать конкретный браузер (ещё есть msedge, разные версии и прочее) и другие команды:
```
playwright install firefox                              # Установить конкретный браузер последней версии
playwright install chromium --channel=chrome-beta       # Установить определенную версию
playwright install --dry-run                            # Показать список установленных браузеров
playwright install --with-deps                          # Установить браузеры для CI (надо sudo)
playwright uninstall chromium                           # Удалить браузер
```

## **Запуск авто-тестов**
### Pytest
* Запуск содержимого директории вида тестов.
* Виды: `smoke`, `accept`, `api` и `load`, например:
```
pytest test/smoke
```
* Запуск по маркерам `pytest`'а (фикстура `pytest.mark` и файл `pytest.ini`).
* Маркеры: `smoke`, `accept`, `core` и `test`, например:
```
pytest -m "smoke"
```
* Прочие команды `pytest`:
```
pytest --browser firefox                        # выбор браузера (chromium, webkit) (если описаны в pytest.ini)
pytest --headless true                          # скрыть браузер (если описаны в pytest.ini)
pytest -k "name"                                # пуск тестов по имени
pytest -n 4                                     # пуск тестов паралельно (потоки процессора)
pytest --alluredir=reports/allure-results       # пуск тестов с отчетом

Полная команда может выглядеть так:
pytest test/smoke --browser firefox --headless true --alluredir=reports/allure-results
```

## **Покрытые авто-тестами модули**
* Авторизация (page/login/...)
* Товары (page/inventory/...)
* Корзина (page/cart/...)
* Покупка (page/cart/...)

## **Архитектура проекта**
```
/test-projectname/                  # корневой каталог (репозиторий) проекта авто-тестов
├── /page/                          # page object модели
│   ├── __init__.py
│   │   /module_page/               # папка с page object моделью и данными модуля
│   │   ├── __init__.py
│   │   ├── module_page.py          # page object класс модуля
│   │   ├── module_locators.py      # селекторы элементов модулей
│   │   └── module_data.py          # тестовые данные модуля
│   └── base_page.py                # базовый page object класс (основные методы работы со страницей)
├── /test/                          # тестовые сценарии с группировкой по видам
│   ├── __init__.py
│   ├── /smoke/                     # дымы (фронт)
│   │   └── test_module.py
│   ├── /accept/                    # приемка (фронт)
│   │   └── test_module.py
│   ├── /api/                       # апи (бэк)
│   │   └── test_module_api.py
│   ├── /load/                      # нагрузочное (locust)
│   └────── locust_smoke.py
├── /report/                        # отчеты и артефакты (если не подключено хранение в jenkins)
│   ├── /screenshots/               # скриншоты
│   ├── /allure-results/            # allure отчеты
│   ├── /pytest-html/               # pytest отчеты
│   ├── /locust/                    # locust отчеты нагрузочного
│   └── /logs/                      # логи выполнения тестов
├── /config/                        # конфигурации
│   ├── __init__.py
│   ├── conftest.py                 # фикстуры pytest
│   └── logger.py                   # конфигурация логирования
├── /utils/                         # вспомогательные инструменты
│   ├── __init__.py
│   ├── /drivers/                   # веб-драйвера и портативные браузеры
│   ├── actions.py                  # сложные методы и действия на страницах
│   ├── asserts.py                  # проверки
│   └── helpers.py                  # вспомогательные элементы
├── /docs/                          # документация
│   ├── PLAN.md                     # документация проекта, план автоматизации, тест-кейсы и история изменений
│   ├── CODE.md                     # описание стиля кода в проекте
│   └── GIT.md                      # описание работы с git и bitbucket
├── pytest.ini                      # конфигурация тестов
├── requirements.txt                # зависимости
├── README.md                       # описание проекта
└── .gitignore                      # игнор лист git
```
* Отчеты и артефакты папки `report` только для локального хранения, в эксплуатации подразумевается хранение артефактов в `jenkins`.

## **Работа в репозитории**
* **Пример безопасного workflow в `git`**
```
# Перед началом работы
git pull origin main

# После нужных изменений и ревью сформируйте инlекс
git add .

# Проверить, что нет лишних файлов
git status

# Создание коммита
git commit -m "Комментарий"

# Отправка изменений на сервер
git push origin main
```
#### **Подключение к репозиторию через `git`**:
* Описано в файле `GIT.md` в папке `docs` в корневой директории проекта