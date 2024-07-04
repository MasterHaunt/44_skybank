## Домашее задание по уроку 11.2

## "Декораторы"

Выполнил: Чельтёмов Андрей Владимирович, поток PD 52/0

### В данной работе:
* Создан модуль `decorators.py`.
* В модуле `decorators.py` написана функция-декоратор `"log"`, которая выводит результат работы функции, обёрнутой декоратором `"log"`: <ок> либо описание ошибки и параметры, с которыми функция была вызвана:
  * если декоратору передано имя файла в параметр `filename` - результаты работы записывает в указанный файл.
  * если декоратору имя файла в параметр `filename` не передавалось - результаты работы функции выводятся в консоль.
* В пакете `tests` создан модуль `test_decorators.py`, в котором реализовано тестирование функции-декоратора `"log"`: написана функция деления числа на переменную - `example_function`, реализовано тестирование декоратора `"log"`: `test_log_decorator_zero_div_err` - при вызове функции с переменной в значении 0 (вызов исключения "деление на ноль"), `test_log_decorator_type_err` - при вызове функции с переменной строкового типа (вызов исключения "несоответствие типов"), а также три функции тестирования записи логов в файл: `test_log_decorator_success_logging` - при успешном выполнении функции `example_function`, `test_log_decorator_zero_div_err_logging` - при вызове функции с переменной в значении 0 (поиск в лог-файле ошибки "деление на ноль"), `test_log_decorator_type_err_logging` - при вызове функции с переменной строкового типа (поиск в лог-файле ошибки "несоответствие типов").
* В пакете `tests` создан модуль `test_decorators_console.py`, в котором реализовано тестирование функции-декоратора `"log"`: написана функция деления числа на переменную - `example_function_console`, реализовано тестирование декоратора `"log"`: `test_log_decorator_success_console` - при успешном выполнении функции `example_function`, `test_log_decorator_zero_div_err_console` - при вызове функции с переменной в значении 0 (поиск в консоли вывода ошибки "деление на ноль"), `test_log_decorator_type_err_console` - при вызове функции с переменной строкового типа (поиск в консоли вывода ошибки "несоответствие типов").

### Функционал, реализованный ранее:
* Создан модуль `generators.py`.
* В модуле `generators.py` написана функция-генератор `card_number_generator`, которая создаёт номера карт в формате `XXXX XXXX XXXX XXXX`, последние цифры берутся из диапазона от `start_index` до `stop_index` включительно.
* В модуле `generators.py` написана функция `filter_by_currency`, выбирающая из списка словарей с информацией о транзакциях те транзакции, которые выполнены в валюте, указанной в параметре `currency`.
* В модуле `generators.py` написана функция `transaction_descriptions`, выбирающая из списка словарей с информацией о транзакциях значения по ключу `description` ("описание")
* В пакете `tests` в модуле `conftests.py` добавлена фикстура, возвращающая список словарей с информацией о транзакциях для последующего использования функциями из модулей `generators.py` и `test_generators.py` 
* В пакете `tests` создан модуль `test_generators.py`, в котором реализовано тестирование функций `card_number_generator`, `filter_by_currency` и `transaction_descriptions`. 

Реализовано проведение тестов ранее написанных модулей:
* В пакете `tests` созданы модули: `conftest.py`, `test_masks.py`, `test_processing.py`, `test_widget.py`. 
* В модуле `conftest.py` написана фикстура `transactions_list`, содержащая информацию о транзакциях для последующего использования в тестировании.
* В модуле `test_masks.py` написаны две функции тестирования: `test_get_mask_card_number` - тестирует работу функции маскировки номера банковской карты, `test_get_mask_account` - тестирует работу функции маскировки номера банковского счёта. Обе функции тестирования используют параметризацию.
* В модуле `test_processing.py` написаны семь функций тестирования, использующие фикстуру из модуля `conftest.py`: четыре тестируют работу функции `processing.filter_by_state` (отбор по признаку `"state": 'EXECUTED'`, по умолчанию, `CANCELED` и не валидное значение `DROPPED`); три - работу функции `processing.sort_by_date` (сортировка по дате: по убыванию, по умолчанию и по возрастанию).
* В модуле `test_widget.py` написаны две функции тестирования: `test_transaction_date` - тестирует работу функции преобразования времени проведения транзакции в дату формата "ДД.ММ.ГГГГ", `test_mask_account_card` - тестирует работу функции маскировки номера банковского счёта/банковской карты. Обе функции тестирования используют параметризацию.
* Исправлена ошибка в функции маскировки номера карты в модуле `masks.py`.
* Модули, использовавшиеся для тестирования функций в предыдущих версиях проекта, удалены.

В модуле `processing.py` реализованы функции:

* `filter_by_state`: принимает на вход список словарей с информацией о транзакциях и возвращает список словарей с информацией о транзакциях, которые были исполнены (`"state" = "EXECUTED"`, по умолчанию). Если помимо списка словарей в функцию передан второй параметр в значении `"CANCELED"` - возвращается список словарей с информацией об отменённых транзакциях.
* `sort_by_date`: принимает на вход список словарей с информацией о транзакциях и возвращает его отсортированным:
    - если второй параметр не передан или передан в значении `"True"` -> по убыванию (от ранних к поздним);
    - если второй параметр передан в значении `"False"` -> по возрастанию (от последних к ранним).

В модуле `masks.py` реализованы функции:

* `get_mask_card_number`: маскирует номер банковской карты в формат: **"<Платёжная система> 0000 00** **** 0000"**
* `get_mask_account`: маскирует номер банковского счёта в формат: **"Счет **0000"**

В модуле `widget.py` реализованы функции:

* `mask_account_card`: маскирует номер банковской карты или номер банковского счёта, используя функции из модуля `masks.py`: `get_mask_card_number` и `get_mask_account` 
* `transaction_date`: возвращает дату проведения транзакции в формате **"ДД.ММ.ГГГГ"**