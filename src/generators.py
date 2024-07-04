def card_number_generator(start_index: int, stop_index: int):
    """Функция-генератор номеров банковских карт. Принимает на вход два целых числа: 'start_index', 'stop_index' -
    первый и последний номер соответственно. При каждом вызове возвращает строку с номером банковской карты в формате
    ХХХХ ХХХХ ХХХХ ХХХХ, последние цифры которого берутся из промежутка от 'start_index' до 'stop_index' включительно
    """
    while start_index <= stop_index:
        free_digits = 16 - len(str(start_index))
        new_card_number = ""
        for i in range(free_digits):
            new_card_number += "0"
        new_card_number += str(start_index)
        new_card_number = (
            new_card_number[0:4]
            + " "
            + new_card_number[4:8]
            + " "
            + new_card_number[8:12]
            + " "
            + new_card_number[12:]
        )
        start_index += 1
        yield new_card_number


def filter_by_currency(transactions: list[dict], currency: str):
    """Функция-генератор, принимает на вход список словарей 'transactions' с информацией о транзакциях и код валюты
    'currency', по которому должна проводиться фильтрация. При каждом вызове функция возвращает словарь с информацией
    о транзакции, проведённой в валюте, указанной в параметре 'currency'"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]):
    """Функция-генератор, принимает на вход список словарей 'transactions' с информацией о транзакциях.
    При каждом вызове функция возвращает значение очередного словаря по ключу 'description' (описание)"""
    for transaction in transactions:
        yield transaction["description"]
