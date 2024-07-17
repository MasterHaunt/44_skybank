from src import masks, utils, processing


def main_menu():
    """Функция выводит приветствие и запрашивает у пользователя источник информации о транзакциях: JSON-файл,
    CSV-файл, XLSX-файл. На выходе функция возвращает информацию о транзакциях.
    При вводе цифры < 0 > программа завершает работу"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. \n\nВыберите необходимый пункт меню:"
          "\n1. Получить информацию о транзакциях из JSON-файла"
          "\n2. Получить информацию о транзакциях из CSV-файла"
          "\n3. Получить информацию о транзакциях из XLSX-файла")
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
                transactions = utils.import_csv_transactions(target_file)
                break
            elif menu_input == "3":
                print("Для обработки выбран XLSX-файл")
                target_file = "data/transactions_excel.xlsx"
                transactions = utils.import_xlsx_transactions(target_file)
                break
            else:
                print("Некорректный выбор. Повторите ввод, либо введите \"0\" для выхода.")
        else:
            print("Некорректный выбор. Повторите ввод, либо введите \"0\" для выхода.")
    return transactions


def select_options() -> dict:
    """Функция последовательно запрашивает у пользователя опции для фильтрации и вывода информации о транзакциях.
    На выходе возвращает словарь со значениями, указанными пользователем"""

    #создание пустого словаря
    options = {}
    # Запуск бесконечного цикла запроса. Выход из цикла с выбором значения для фильтрации данных происходит
    # при вводе значений "EXECUTED", "CANCELED" или "PENDING". При вводе значения "0" программа завершит работу
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию."
              "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
              "\n(для выхода из программы введите \"0\" )")
        sorting_state = input("STATE: ").upper()
        if sorting_state == "0":
            exit("Программа завершила работу")
        elif sorting_state in ("EXECUTED", "CANCELED", "PENDING"):
            options["sorting_state"] = sorting_state
            break
        else: print(f"Статус операции {sorting_state} недоступен")

    # Запуск бесконечного цикла запроса. Выход из цикла с выбором опции сортировки транзакций по дате происходит
    # при вводе значений "да" или "нет". При вводе значения "0" программа завершит работу
    while True:
        print("Отсортировать транзакции по дате?"
              "\n (да / нет)"
              "\n (для выхода из программы введите \"0\" )")
        sort_by_date = input("Ввод: ").lower()
        if sort_by_date == "0":
            exit("Программа завершила работу")
        elif sort_by_date == "да":
            options["sort_by_date"] = True
            break
        elif sort_by_date == "нет":
            options["sort_by_date"] = False
            break
        else: print(f"Ответ введён некорректно: {sort_by_date}. Повторите ввод.")

    if options["sort_by_date"]:
        # Если выбрана сортировка транзакций по дате: Запуск бесконечного цикла запроса. Выход из цикла с выбором
        # направления сортировки происходит при вводе значений "по возрастанию" или "по убыванию".
        # При вводе значения "0" программа завершит работу
        while True:
            print("Отсортировать транзакции по возрастанию / по убыванию ?"
                    "\n (по возрастанию / по убыванию)"
                    "\n (для выхода из программы введите \"0\" )")
            ascending = input("Ввод: ").lower()
            if ascending == "0":
                exit("Программа завершила работу")
            elif ascending == "по возрастанию":
                options["ascending"] = True
                break
            elif ascending == "по убыванию":
                options["ascending"] = False
                break
            else:
                print(f"Ответ введён некорректно: {ascending}. Повторите ввод.")

    # Запуск бесконечного цикла запроса. Выход из цикла с выбором отображения всех транзакций (ввод "нет") или
    # только рублевых транзакций (ввод "да"). При вводе значения "0" программа завершит работу
    while True:
        print("Показывать только рублевые транзакции ?"
                      "\n (да / нет)"
                      "\n (для выхода из программы введите \"0\" )")
        show_only_rub = input("Ввод: ").lower()
        if show_only_rub == "0":
            exit("Программа завершила работу")
        elif show_only_rub == "да":
            options["show_only_rub"] = True
            break
        elif show_only_rub == "нет":
            options["show_only_rub"] = False
            break
        else: print(f"Ответ введён некорректно: {show_only_rub}. Повторите ввод.")

    # Запуск бесконечного цикла запроса. Выход из цикла с выбором опции отбора транзакций по содержанию определённого
    # слова в описании транзакции (ввод "да"), либо вывод всех транзакций (ввод "нет").
    # При вводе значения "0" программа завершит работу
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании?"
              "\n (да / нет)"
              "\n (для выхода из программы введите \"0\" )")
        sort_by_query = input("Ввод: ").lower()
        if sort_by_query == "0":
            exit("Программа завершила работу")
        elif sort_by_query == "да":
            options["sort_by_query"] = True
            break
        elif sort_by_query == "нет":
            options["sort_by_query"] = False
            break
        else: print(f"Ответ введён некорректно: {sort_by_query}. Повторите ввод.")

    # Если выбрана фильтрация транзакций по слову в описании: запрос слова, которое программа будет искать в
    # описаниях транзакций (поле "description")
    if options["sort_by_query"]:
        options["query"] = input("Ввод: ").lower()
    return options


#def main():


if __name__ == "__main__":
    print(select_options())
