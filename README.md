## Домашее задание по уроку 13.2

## "Библиотеки re, collections, random"

Выполнил: Чельтёмов Андрей Владимирович, поток PD 52/0

### В данной работе:
В модуле `processing.py` реализованы функции:
* `search_in_transactions`, которая принимает на вход список словарей с информацией о транзакциях и текстовую строку для поиска, а возвращает список словарей с информацией о тех транзакциях, в описании (поле 'description') которых присутствует текст из строки для поиска
* `transactions_by_categories`, которая принимает на вход список словарей с информацией о транзакциях и список с названиями категорий операций, а возвращает словарь, в котором ключи - наименования категорий операций, а значения - количества операций соответствующих категорий
В модуле `test_processing.py` реализовано тестирование функций `search_in_transactions` и `transactions_by_categories`
В модуле `utils.py` реализованы функции:
* `df_string_to_dict` - преобразует строку датафрейма с информацией о транзакции в словарь заданного формата. Если поле "id" не содержит символ "."(признак вещественного числа), то создаётся пустой словарь для последующего исключения из итогового списка;
* `dataframe_to_list_of_dicts` - принимает на вход датафрейм с информацией о транзакциях, преобразует каждую строку датафрейма функцией `df_string_to_dict`, затем собирает преобразованные строки в список словарей. Пустой словарь в список не добавляется;
В модуле `main.py` реализованы функции:
* `get_transactions`, которая выводит приветствие и запрашивает у пользователя источник информации о транзакциях: `JSON`-файл, `CSV`-файл, `XLSX`-файл. На выходе функция возвращает информацию о транзакциях. При вводе цифры `< 0 >` программа завершает работу;
* `select_options`, которая последовательно запрашивает у пользователя опции для фильтрации и вывода информации о транзакциях. В любой момент при вводе цифры `< 0 >` программа завершает работу. На выходе возвращает словарь со значениями, указанными пользователем;
* `main_processing` - функция отбора информации о транзакциях по введённым пользователем критериям. На вход принимает список словарей с информацией о транзакциях и словарь с критериями отбора и сортировки. Возвращает список словарей, отобранный и отсортированный по заданным критериям, , вызывая функции из модуля `processing.py`: `filter_by_state`, `sort_by_date`, `search_in_transactions`, `transactions_by_currency`;
* `main` - Функция принимает на вход список словарей, с информацией о транзакциях и словарь с критериями отбора и сортировки и передаёт их в функцию main_processing, после чего выводит список отобранных и отсортированных транзакций, преобразуя дату транзакции функцией `transaction_date` и маскируя номера банковских карт и счетов с использованием функции `mask_account_card` из модуля `widget.py`

### Функционал, реализованный ранее:
В пакете `src` :
* В модуле `utils.py` реализована функция `import_xlsx_transactions` - чтение и преобразование информации о транзакциях из файла *.xlsx. На вход принимает имя файла с данными о транзакциях, на выходе возвращает датафрейм из полученного файла. Если файл с указанным именем пуст или отсутствует - функция вернёт [] ( пустой список ); 
* В модуле `utils.py` реализована функция `import_csv_transactions` - чтение и преобразование информации о транзакциях из файла *.csv. На вход принимает имя файла с данными о транзакциях, на выходе возвращает датафрейм из полученного файла. Если файл с указанным именем пуст или отсутствует - функция вернёт [] ( пустой список );
В пакете `tests` :
* В модуле  `test_utils.py` реализовано тестирование функций `import_xlsx_transactions` и `import_csv_transactions`.


* В модулях `masks.py` и `utils.py` добавлено логирование выполнения функций в файлы `/logs/masks.log` и `/logs/utils.log/` соответственно;
* Исправлены некоторые  ошибки аннотации типов в пакете `src`.

* В проект добавлена директория `data`, в которую помещён файл `operations.json` с json-записями о транзакциях;
* В проект добавлен (без включения в репозиторий) файл `.env`, в который записан api-ключ к сайту `https://apilayer.com/`, а также (с добавлением в репозиторий) файл `.envtemplate`, в который записан пример api-ключа;
* В пакете `src` созданы модули `config.py`, `utils.py` и `external_api.py`;
* В модуле `config.py` записана константа `ROOT_PATH` - путь к корневому каталогу проекта из пакета `src`;
* В модуле `utils.py` реализована функция `import_json_transactions` - чтение и преобразование информации о транзакциях из файла *.json. На вход принимает имя файла с данными о транзакциях, на выходе возвращает список словарей, десериализованных из полученного файла. Если файл с указанным именем пуст или отсутствует - функция вернёт [] ( пустой список );
* В модуле `external_api.py` реализована функция `transaction_converting_to_rubles` - расчёт суммы транзакции в Российских рублях. Принимает на вход данные о транзакции и возвращает сумму транзакции в Российских рублях. Если транзакция проведена в валюте, отличной от рублей, функция обращается к внешнему API, используя ключ из файла с переменными окружения .env, с запросом на пересчёт суммы транзакции в рубли;
* В пакете `tests` создан модуль `test_utils.py`, в котором реализовано тестирование функции `import_json_transactions`. Вместо функции загрузки информации о транзакциях, которая мспользуется в тестируемой функции, подставлен объект Mock, возвращающий данные об одной транзакции в требуемом виде;
* В пакете `tests` создан модуль `test_external_api.py`, в котором реализовано тестирование функции `transaction_converting_to_rubles` при помощи декоратора `@patch`.

* Создан модуль `decorators.py`.
* В модуле `decorators.py` написана функция-декоратор `"log"`, которая выводит результат работы функции, обёрнутой декоратором `"log"`: <ок> либо описание ошибки и параметры, с которыми функция была вызвана:
  * если декоратору передано имя файла в параметр `filename` - результаты работы записывает в указанный файл.
  * если декоратору имя файла в параметр `filename` не передавалось - результаты работы функции выводятся в консоль.
* В пакете `tests` создан модуль `test_decorators.py`, в котором реализовано тестирование функции-декоратора `"log"`: написана функция деления числа на переменную - `example_function`, реализовано тестирование декоратора `"log"`: `test_log_decorator_zero_div_err` - при вызове функции с переменной в значении 0 (вызов исключения "деление на ноль"), `test_log_decorator_type_err` - при вызове функции с переменной строкового типа (вызов исключения "несоответствие типов"), а также три функции тестирования записи логов в файл: `test_log_decorator_success_logging` - при успешном выполнении функции `example_function`, `test_log_decorator_zero_div_err_logging` - при вызове функции с переменной в значении 0 (поиск в лог-файле ошибки "деление на ноль"), `test_log_decorator_type_err_logging` - при вызове функции с переменной строкового типа (поиск в лог-файле ошибки "несоответствие типов").
* В пакете `tests` создан модуль `test_decorators_console.py`, в котором реализовано тестирование функции-декоратора `"log"`: написана функция деления числа на переменную - `example_function_console`, реализовано тестирование декоратора `"log"`: `test_log_decorator_success_console` - при успешном выполнении функции `example_function`, `test_log_decorator_zero_div_err_console` - при вызове функции с переменной в значении 0 (поиск в консоли вывода ошибки "деление на ноль"), `test_log_decorator_type_err_console` - при вызове функции с переменной строкового типа (поиск в консоли вывода ошибки "несоответствие типов").


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