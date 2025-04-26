# Архитектура проекта
## Универсальная архитектура папок 1
* Проект содержится в отдельной папке test-projectname
* Есть возможность хранить несколько "независимых проектов в одной директории"
```
/test-project                       # корневая папка (или основная папка репозитория) проекта авто-тестов
    /test-projectname                   # папка проекта авто-тестов приложения
        /page                               # page object модели
            __init__.py
            base_page.py                        # базовый класс (основные методы работы со страницей)
            module_page.py                      # класс модуля
        /data                           # тестовые данные и 
            __init__.py
            /locators                       # селекторы и элементы
                __init__.py
                module_locators.py              # селекторы элементов модулей
            /data                           # тестовые данные
                __init__.py
                module_data.py                  # тестовые данные модуля
        /test                           # тестовые сценарии с группировкой по видам
            __init__.py
            /smoke                          # дымы
                test_module.py
            /accept                         # приемка
                test_module.py
            /api                            # апи \ бэк
                test_module_api.py
            /load                           # нагрузочное
                locust_smoke.py
        /reports                        # отчетность
            /screenshots                    # скриншоты
            /allure-results                 # аллюр отчеты
            /pytest-html                    # pytest отчеты
            /locust                         # locust отчеты
    /config                             # конфигурации
        __init__.py                         
        conftest.py                         # фикстуры pytest
        logger.py                           # конфигурация логирования
    /utils                              # вспомогательные инструменты
        __init__.py
        /drivers                            # веб-драйвера и портативные браузеры
        actions.py                          # сложные методы и действия на страницах
        asserts.py                          # проверки
        helpers.py                          # вспомогательные элементы
    /docs                               # документация
        ARCHITECTURE.md                     # описание архитектуры проекта
        CODE.md                             # описание стиля кода в проекте
        GIT.md                              # описание работы с git и bitbucket
        PLAN.md                             # Документация проекта тестов, план авто-тестирования, описание тест-кейсов и изменений в тестах
    pytest.ini                          # конфигурация тестов
    requirements.txt                    # зависимости
    README.md                           # описание проекта
    .gitignore                          # игнор лист git
```
## Универсальная архитектура папок 2
* Самый распространённый формат директорий
```
/test-project                       # корневая папка (или основная папка репозитория) проекта авто-тестов
    /page                               # page object модели
        __init__.py
        base_page.py                        # базовый класс (основные методы работы со страницей)
        module_page.py                      # класс модуля
    /data                               # тестовые данные и 
        __init__.py
        /locators                           # селекторы и элементы
            __init__.py
            module_locators.py                  # селекторы элементов модулей
        /data                               # тестовые данные
            __init__.py
            module_data.py                      # тестовые данные модуля
    /test                               # тестовые сценарии с группировкой по видам
        __init__.py
        /smoke                              # дымы
            test_module.py
        /accept                             # приемка
            test_module.py
        /api                                # апи \ бэк
            test_module_api.py
        /load                               # нагрузочное
            locust_smoke.py
    /reports                            # отчетность
        /screenshots                        # скриншоты
        /allure-results                     # аллюр отчеты
        /pytest-html                        # pytest отчеты
        /locust                             # locust отчеты
    /config                             # конфигурации
        __init__.py                         
        conftest.py                         # фикстуры pytest
        logger.py                           # конфигурация логирования
    /utils                              # вспомогательные инструменты
        __init__.py
        /drivers                            # веб-драйвера и портативные браузеры
        actions.py                          # сложные методы и действия на страницах
        asserts.py                          # проверки
        helpers.py                          # вспомогательные элементы
    /docs                               # документация
        ARCHITECTURE.md                     # описание архитектуры проекта
        CODE.md                             # описание стиля кода в проекте
        GIT.md                              # описание работы с git и bitbucket
        PLAN.md                             # Документация проекта тестов, план авто-тестирования, описание тест-кейсов и изменений в тестах
    pytest.ini                          # конфигурация тестов
    requirements.txt                    # зависимости
    README.md                           # описание проекта
    .gitignore                          # игнор лист git
```
## Универсальная структура директорий проекта 3 (оптимальный)
* Удобный формат директорий объединяющей все ресурсы page object модели модуля в одном месте
```
/test-projectname                   # корневой каталог (репозиторий) проекта авто-тестов
    /page                               # page object модели
        __init__.py
        /module_page                        # папка с page object моделью и данными модуля
            __init__.py
            module_page.py                      # page object класс модуля
            module_locators.py                  # селекторы элементов модулей
            module_data.py                      # тестовые данные модуля
        base_page.py                        # базовый page object класс (основные методы работы со страницей)
    /test                               # тестовые сценарии с группировкой по видам
        __init__.py
        /smoke                              # дымы (фронт)
            test_module.py
        /accept                             # приемка (фронт)
            test_module.py
        /api                                # апи (бэк)
            test_module_api.py
        /load                               # нагрузочное (locust)
            locust_smoke.py
    /report                             # отчеты и артефакты (если не подключено хранение в jenkins)
        /screenshots                        # скриншоты
        /allure-results                     # allure отчеты
        /pytest-html                        # pytest отчеты
        /locust                             # locust отчеты нагрузочного
        /logs                               # логи выполнения тестов
    /config                             # конфигурации
        __init__.py
        conftest.py                         # фикстуры pytest
        logger.py                           # конфигурация логирования
    /utils                              # вспомогательные инструменты
        __init__.py
        /drivers                            # веб-драйвера и портативные браузеры
        actions.py                          # сложные методы и действия на страницах
        asserts.py                          # проверки
        helpers.py                          # вспомогательные элементы
    /docs                               # документация
        PLAN.md                             # документация проекта, план автоматизации, тест-кейсы и история изменений
        CODE.md                             # описание стиля кода в проекте
        GIT.md                              # описание работы с git и bitbucket
    pytest.ini                          # конфигурация тестов
    requirements.txt                    # зависимости
    README.md                           # описание проекта
    .gitignore                          # игнор лист git
```
* Альтернативный вариант демонстрации директорий 3:
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