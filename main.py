from src import utils, processing, widget


def get_transactions():
    """Функция выводит приветствие и запрашивает у пользователя источник информации о транзакциях: JSON-файл,
    CSV-файл, XLSX-файл. На выходе функция возвращает информацию о транзакциях.
    При вводе цифры < 0 > программа завершает работу"""
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями. \n\nВыберите необходимый пункт меню:"
        "\n1. Получить информацию о транзакциях из JSON-файла"
        "\n2. Получить информацию о транзакциях из CSV-файла"
        "\n3. Получить информацию о транзакциях из XLSX-файла"
    )
    # Запуск бесконечного цикла запроса. Выход из цикла с выбором соответствующего источника данных происходит
    # при вводе значений "1", "2" или "3". При вводе значения "0" программа завершит работу
    while True:
        menu_input = input("Введите номер пункта меню: ")
        if menu_input.isdigit():
            if menu_input == "0":
                exit("Программа завершила работу")
            elif menu_input == "1":
                print("Для обработки выбран JSON-файл")
                target_file = "data/operations.json"
                transactions = utils.import_json_transactions(target_file)
                break
            elif menu_input == "2":
                print("Для обработки выбран CSV-файл")
                target_file = "data/transactions.csv"
                transactions = utils.dataframe_to_list_of_dicts(utils.import_csv_transactions(target_file))
                break
            elif menu_input == "3":
                print("Для обработки выбран XLSX-файл")
                target_file = "data/transactions_excel.xlsx"
                transactions = utils.dataframe_to_list_of_dicts(utils.import_xlsx_transactions(target_file))
                break
            else:
                print('Некорректный выбор. Повторите ввод, либо введите "0" для выхода.')
        else:
            print('Некорректный выбор. Повторите ввод, либо введите "0" для выхода.')
    return transactions


def select_options() -> dict:
    """Функция последовательно запрашивает у пользователя опции для фильтрации и вывода информации о транзакциях.
    На выходе возвращает словарь со значениями, указанными пользователем"""

    # создание пустого словаря
    options = {}
    # Запуск бесконечного цикла запроса. Выход из цикла с выбором значения для фильтрации данных происходит
    # при вводе значений "EXECUTED", "CANCELED" или "PENDING". При вводе значения "0" программа завершит работу
    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
            '\n(для выхода из программы введите "0" )'
        )
        sorting_state = input("STATE: ").upper()
        if sorting_state == "0":
            exit("Программа завершила работу")
        elif sorting_state in ("EXECUTED", "CANCELED", "PENDING"):
            options["state"] = sorting_state
            break
        else:
            print(f"Статус операции <{sorting_state}> недоступен")

    # Запуск бесконечного цикла запроса. Выход из цикла с выбором опции сортировки транзакций по дате происходит
    # при вводе значений "да" или "нет". При вводе значения "0" программа завершит работу
    while True:
        print("Отсортировать транзакции по дате?" "\n (да / нет)" '\n (для выхода из программы введите "0" )')
        sort_by_date = input("Ввод: ").lower()
        if sort_by_date == "0":
            exit("Программа завершила работу")
        elif sort_by_date == "да":
            options["sort_by_date"] = True
            break
        elif sort_by_date == "нет":
            options["sort_by_date"] = False
            break
        else:
            print(f"Ответ введён некорректно: <{sort_by_date}>. Повторите ввод.")

    if options["sort_by_date"]:
        # Если выбрана сортировка транзакций по дате: Запуск бесконечного цикла запроса. Выход из цикла с выбором
        # направления сортировки происходит при вводе значений "по возрастанию" или "по убыванию".
        # При вводе значения "0" программа завершит работу
        while True:
            print(
                "Отсортировать транзакции по возрастанию / по убыванию ?"
                "\n (по возрастанию / по убыванию)"
                '\n (для выхода из программы введите "0" )'
            )
            descending = input("Ввод: ").lower()
            if descending == "0":
                exit("Программа завершила работу")
            elif descending == "по возрастанию":
                options["descending"] = False
                break
            elif descending == "по убыванию":
                options["descending"] = True
                break
            else:
                print(f"Ответ введён некорректно: <{descending}>. Повторите ввод.")

    # Запуск бесконечного цикла запроса. Выход из цикла с выбором отображения всех транзакций (ввод "нет") или
    # только рублевых транзакций (ввод "да"). При вводе значения "0" программа завершит работу
    while True:
        print("Показывать только рублевые транзакции ?" "\n (да / нет)" '\n (для выхода из программы введите "0" )')
        show_only_rub = input("Ввод: ").lower()
        if show_only_rub == "0":
            exit("Программа завершила работу")
        elif show_only_rub == "да":
            options["show_only_rub"] = True
            break
        elif show_only_rub == "нет":
            options["show_only_rub"] = False
            break
        else:
            print(f"Ответ введён некорректно: <{show_only_rub}>. Повторите ввод.")

    # Запуск бесконечного цикла запроса. Выход из цикла с выбором опции отбора транзакций по содержанию определённого
    # слова в описании транзакции (ввод "да"), либо вывод всех транзакций (ввод "нет").
    # При вводе значения "0" программа завершит работу
    while True:
        print(
            "Отфильтровать список транзакций по определенному слову в описании?"
            "\n (да / нет)"
            '\n (для выхода из программы введите "0" )'
        )
        sort_by_query = input("Ввод: ").lower()
        if sort_by_query == "0":
            exit("Программа завершила работу")
        elif sort_by_query == "да":
            options["sort_by_query"] = True
            break
        elif sort_by_query == "нет":
            options["sort_by_query"] = False
            break
        else:
            print(f"Ответ введён некорректно: <{sort_by_query}>. Повторите ввод.")

    # Если выбрана фильтрация транзакций по слову в описании: запрос слова, которое программа будет искать в
    # описаниях транзакций (поле "description")
    if options["sort_by_query"]:
        options["query"] = input("Введите ключевое слово для поиска: ").lower()
    return options


def main_processing(transactions: list[dict], options: dict) -> list[dict]:
    """функция отбора информации о транзакциях по введённым пользователем критериям.
    На вход принимает список словарей с информацией о транзакциях и словарь с критериями отбора и сортировки.
    Возвращает список словарей, отобранный и отсортированный по заданным критериям, вызывая функции из модуля
    processing.py: filter_by_state, sort_by_date, search_in_transactions, transactions_by_currency"""

    # print(transactions)
    # print(options)
    result = processing.filter_by_state(transactions, options["state"])
    if options["sort_by_date"]:
        result = processing.sort_by_date(transactions=result, descending=options["descending"])
    if options["sort_by_query"]:
        result = processing.search_in_transactions(result, options["query"])
    if options["show_only_rub"]:
        result = processing.transactions_by_currency(result, "RUB")
    return result


def main(user_transactions: list[dict], user_options: dict):
    """Функция принимает на вход список словарей, с информацией о транзакциях и словарь с критериями отбора и
    сортировки и передаёт их в функцию main_processing, после чего выводит список отобранных и отсортированных
    транзакций, преобразуя дату транзакции функцией transaction_date и маскируя номера банковских карт и счетов с
    использованием функции mask_account_card из модуля widget.py"""
    processed_transactions = main_processing(user_transactions, user_options)
    if len(processed_transactions) == 0:
        print("Выборка по заданным параметрам пуста!")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(processed_transactions)}")
        for transaction in processed_transactions:
            print(f"\n{widget.transaction_date(transaction.get("date", ""))} {transaction.get("description", "")}")
            print(
                f"{widget.mask_account_card(transaction.get("from", ""))} -> {widget.mask_account_card(transaction.get("to", ""))}"
            )
            print(
                f"Сумма: {transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]}"
            )


if __name__ == "__main__":
    main(get_transactions(), select_options())
