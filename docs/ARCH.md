# Архитектуры проекта
## Универсальная архитектура папок 1
* Проект содержится в отдельной папке test-projectname
* Есть возможность хранить несколько относительно независимых проектов в одной директории
```
/test-project                       # корневая папка (или основная папка репозитория) проекта авто-тестов
    /test-projectname                   # папка проекта авто-тестов приложения
        /page                               # page object модели
            __init__.py
            base_page.py                        # базовый класс (основные методы работы со страницей)
            module_page.py                      # класс модуля
        /resources                          # тестовые данные и локаторы
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
    /config                                 # конфигурации
        __init__.py                         
        conftest.py                             # фикстуры pytest
        logger.py                               # конфигурация логирования
    /utils                                  # вспомогательные инструменты
        __init__.py
        /drivers                                # веб-драйвера и портативные браузеры
        actions.py                              # сложные методы и действия на страницах
        asserts.py                              # проверки
        helpers.py                              # вспомогательные элементы
    /docs                                   # документация
        PLAN.md                                 # Документация проекта тестов, план авто-тестирования, описание тест-кейсов и изменений в тестах
        ARCH.md                                 # описание вариантов архитектур проекта
        MD.md                                   # описание markdown разметки
        CODE.md                                 # описание стиля кода в проекте
        GIT.md                                  # описание работы с git и bitbucket    pytest.ini                          # конфигурация тестов
    requirements.txt                        # зависимости
    README.md                               # описание проекта
    .gitignore                              # игнор лист git
```
## Универсальная архитектура папок 2
* Самый распространённый формат директорий
```
/test-project                       # корневая папка (или основная папка репозитория) проекта авто-тестов
    /page                               # page object модели
        __init__.py
        base_page.py                        # базовый класс (основные методы работы со страницей)
        module_page.py                      # класс модуля
    /resources                          # тестовые данные и локаторы
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
    /reports                            # отчетность
        /screenshots                        # скриншоты
        /allure-results                     # аллюр отчеты
        /pytest-html                        # pytest отчеты
        /locust                             # locust отчеты
    /docs                               # документация
        PLAN.md                             # Документация проекта тестов, план авто-тестирования, описание тест-кейсов и изменений в тестах
        ARCH.md                             # описание вариантов архитектур проекта
        MD.md                               # описание markdown разметки
        CODE.md                             # описание стиля кода в проекте
        GIT.md                              # описание работы с git и bitbucket
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
        /module_1_page                        # папка с page object моделью и данными модуля 1
            __init__.py
            module_1_page.py                      # page object класс модуля 1
            module_1_locators.py                  # селекторы элементов модуля 1
            module_1_data.py                      # тестовые данные модуля 1
        /module_2_page                        # папка с page object моделью и данными модуля 2
            __init__.py
            module_2_page.py                      # page object класс модуля 2 
            module_2_locators.py                  # селекторы элементов модуля 2
            module_2_data.py                      # тестовые данные модуля 2
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
    /report                             # отчеты и артефакты (если не подключено хранение в jenkins)
        /screenshots                        # скриншоты
        /allure-results                     # allure отчеты
        /pytest-html                        # pytest отчеты
        /locust                             # locust отчеты нагрузочного
        /logs                               # логи выполнения тестов
    /docs                               # документация
        PLAN.md                             # документация проекта, план автоматизации, тест-кейсы и история изменений
        ARCH.md                             # описание вариантов архитектур проекта
        MD.md                               # описание markdown разметки
        CODE.md                             # описание стиля кода в проекте
        GIT.md                              # описание работы с git и bitbucket
    pytest.ini                          # конфигурация тестов
    requirements.txt                    # зависимости
    README.md                           # описание проекта
    .gitignore                          # игнор лист git
```
* Альтернативный (графически) вариант демонстрации директорий 3:
```
/test-projectname/                  # корневой каталог (репозиторий) проекта авто-тестов
├── /page/                          # page object модели
│   ├── __init__.py
│   ├── /module_1_page/               # папка с page object моделью и данными модуля 1
│   │   ├── __init__.py
│   │   ├── module_1_page.py          # page object класс модуля 1
│   │   ├── module_1_locators.py      # селекторы элементов модул 2
│   │   └── module_1_data.py          # тестовые данные модуля 2 
│   ├── /module_2_page/               # папка с page object моделью и данными модуля 2
│   │   ├── __init__.py
│   │   ├── module_2_page.py          # page object класс модуля 2
│   │   ├── module_2_locators.py      # селекторы элементов модуля 2
│   │   └── module_2_data.py          # тестовые данные модуля 2
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
├── /report/                        # отчеты и артефакты (если не подключено хранение в jenkins)
│   ├── /screenshots/               # скриншоты
│   ├── /allure-results/            # allure отчеты
│   ├── /pytest-html/               # pytest отчеты
│   ├── /locust/                    # locust отчеты нагрузочного
│   └── /logs/                      # логи выполнения тестов
├── /docs/                          # документация
│   ├── PLAN.md                     # документация проекта, план автоматизации, тест-кейсы и история изменений
│   ├── ARCH.md                     # описание вариантов архитектур проекта
│   ├── MD.md                       # описание markdown разметки
│   ├── CODE.md                     # описание стиля кода в проекте
│   └── GIT.md                      # описание работы с git и bitbucket
├── pytest.ini                      # конфигурация тестов
├── requirements.txt                # зависимости
├── README.md                       # описание проекта
└── .gitignore                      # игнор лист git
```