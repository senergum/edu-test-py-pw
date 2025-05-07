# Инструкция по работе с Python

## 0. Установка Python
### Windows
#### Скачать Python
* Официальный сайт: [**Python 13+**](python.org/downloads)
* Выберите версию 3.13+ (галочка "Add Python to PATH" при установке!).
* Проверка инсталляции пакетов в терминале:
```bash
python --version                            # Проверка основной версии
python -m pip --version                     # Проверка pip
```
* Если команда не работает, добавьте Python в PATH вручную:
  * Панель управления → Система → Дополнительные параметры → Переменные среды → Path → Добавить пути:
    * C:\Python311\ (или ваша версия)
    * C:\Python311\Scripts\ (для pip)
### Linux/macOS
* Python обычно уже установлен. Проверьте:
```bash
python3 --version
```
* Если нет:
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install python3 python3-pip
# macOS (через Homebrew)
brew install python
```

## 1. Настройка окружения
### Где находится Python?
#### Windows
```bash
where python                              # Путь к интерпретатору
where pip                                 # Путь к pip
```
#### Linux/macOS
```bash
which python3
which pip3
```
### Пути установки пакетов
* Пакеты через pip устанавливаются в:
```bash
pip list --path                           # Покажет путь к site-packages
python -m site --user-site                # Локальные пакеты пользователя
python -c "import sys; print(sys.path)"   # Все пути Python
```
### Стандартное местоположение
#### Windows
* Обычно устанавливается в:
  * C:\Users\<Username>\AppData\Local\Programs\Python\Python311\python.exe
* Или (если установлен для всех пользователей):
  * C:\Program Files\Python311\python.exe
* **Pip** и скрипты:
  * C:\Users\<Username>\AppData\Local\Programs\Python\Python311\Scripts\pip.exe
#### Linux/macOS
* **Python 3**:
  * /usr/bin/python3
* **Pip**:
  * /usr/bin/pip3
* Пользовательские **пакеты** (--user):
  * ~/.local/bin/  # (pip install --user добавляет сюда скрипты)
### Виртуальное окружение (venv)
#### Windows
* Активация
  * .venv\Scripts\activate  # (из папки проекта)
* Путь к активационному скрипту
  * .venv\Scripts\activate.bat  # (CMD)
  * .venv\Scripts\Activate.ps1  # (PowerShell)
#### Linux/macOS
* Активация
  * source .venv/bin/activate
* Путь к активационному скрипту
  * .venv/bin/activate
### Где хранятся пакеты в виртуальном окружении?
#### Windows
* .venv\Lib\site-packages\
#### Linux/macOS
* .venv/lib/python3.11/site-packages/
### Проблемы с активацией?
#### Ошибка "Невозможно загрузить файл activate.ps1" (Windows):
* Запустите PowerShell от имени администратора и выполните:
```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
* Ошибка прав (Linux/macOS):
```bash chmod +x .venv/bin/activate```
  * Если нужно добавить что-то ещё (например, про conda или pyenv) — уточните!

## 2. Виртуальные окружения
### Создание и активация
#### Windows
```bash
python -m venv .venv                      # Создать окружение
.venv\Scripts\activate                    # Активировать
```
#### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```
#### Деактивация
```bash
deactivate
```
#### Полезные команды
```bash
pip list                                  # Список установленных пакетов
pip freeze > requirements.txt             # Экспорт зависимостей
pip install -r requirements.txt           # Установка из файла
```

## 3. Запуск скриптов
```bash
python script.py                          # Запуск файла
python -m module_name                     # Запуск модуля
python -c "print('Hello')"                # Запуск кода из строки
```

## 4. Интеграция с IDE (PyCharm, OpenIDE)
* Открытие проекта:
  * File → Open (выберите папку проекта).
* Настройка интерпретатора:
  * File → Settings → Project → Python Interpreter → Add Interpreter:
    * Выберите существующий .venv или создайте новый.
* Запуск кода:
  * ПКМ по файлу → Run (или Shift + F10).

## 5. Типичные проблемы
* Python не найден в терминале
  * Решение: 
    * Добавьте Python в PATH (см. раздел 0).
    * Перезапустите терминал\IDE\ПК.
* Ошибка доступа при установке пакетов
  * pip install --user package_name  # Установка в пользовательскую папку
* Конфликт версий Python
  * python3.11 script.py  # Указание версии
* Ошибка виртуального окружения
  * Set-ExecutionPolicy RemoteSigned -Scope CurrentUser  # Windows (PowerShell)
  * chmod +x .venv/bin/activate           # Linux/macOS

## 6. Полезные команды
```bash
python -m http.server	                  # Запуск веб-сервера в текущей папке
python -m pydoc модуль	                  # Документация модуля
python -m pip install                     # --upgrade pip	Обновление pip
python -m venv --clear .venv	          # Очистка окружения
```

