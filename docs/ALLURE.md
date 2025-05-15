# ALLURE отчёты


## Запуск allure отчётов
### Windows
* Как добавить allure.bat (например лежащий в C:\Users\User\PycharmProjects\allure-2.34.0\bin) в PATH системы
  * Нажмите `Win + S` (Поиск) и введи `Переменные среды`
  * Выбери пункт «Изменение системных переменных среды» («Edit environment variables»)
  * В открывшемся окне `Свойства системы\Дополнительно` выбери `Переменные среды...` 
  * Откроется окно `Переменные среды`, выберите в списке `Системные переменные` строку `Path` и нажмите `Изменить` (или дважды кликните)
  * Откроется окно `Изменить переменную среды`, нажмите `Создать` и введите ваш путь, например:
    ```shell
    C:\Users\User\PycharmProjects\allure-2.34.0\bin
    ```
  * Нажмите ОК во всех открытых окнах, чтобы сохранить изменения.
* Проверка
  * Закройте все терминалы (CMD, PowerShell) и откройте новый.
    * Нажмите `Win + R` и введите `cmd`, нажмите клавишу `enter`
  * Введите команду
    ```shell
    allure --version
    ```
  * Если путь добавлен верно, то увидите версию `allure`  

#### В ручную (CMD)
* Открыть командную строку (CMD или PowerShell)
* Перейти в папку с allure.bat, например
```shell
cd C:\Users\User\PycharmProjects\allure\bin
```
* Запустить генерацию отчёта из папки с результатами (например, reports/allure-results)
```shell
.\allure generate C:\Users\User\PycharmProjects\edu-test\reports\allure-results -o C:\Users\User\PycharmProjects\edu-test\reports\allure-report
```
* После генерации отчёта открыть его локально
```shell
.\allure open C:\Users\User\PycharmProjects\edu-test\reports\allure-report
```
* Альтернативно, запустить сразу serve, который сгенерирует и откроет отчёт и после закрытия удалит временные файлы
```shell
.\allure serve C:\Users\User\PycharmProjects\edu-test\reports\allure-results
```