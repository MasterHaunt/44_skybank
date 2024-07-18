from src import generators


def test_card_number_generator():
    """Тестирование функции-генератора номеров банковских карт. 'start_index' (начальный номер) = 100,
    'stop_index (конечный номер) = 105"""
    card_numbers = generators.card_number_generator(100, 105)
    assert next(card_numbers) == "0000 0000 0000 0100"
    assert next(card_numbers) == "0000 0000 0000 0101"
    assert next(card_numbers) == "0000 0000 0000 0102"
    assert next(card_numbers) == "0000 0000 0000 0103"
    assert next(card_numbers) == "0000 0000 0000 0104"
    assert next(card_numbers) == "0000 0000 0000 0105"


def test_filter_by_currency(adv_transactions_list):
    """Тестирование функции-генератора фильтрации транзакций по заданной валюте.
    Использует фикстуру 'adv_transactions_list' из модуля 'conftest.py'
    Инициализируется два итератора: 'rub_transactions' - для транзакций проведённых в рублях ("RUB"),
    'usd_transactions'  - для транзакций проведённых в долларах США ('USD')"""
    rub_transactions = generators.filter_by_currency(adv_transactions_list, "RUB")
    assert next(rub_transactions)["id"] == 873106923
    assert next(rub_transactions)["id"] == 594226727
    usd_transactions = generators.filter_by_currency(adv_transactions_list, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268
    assert next(usd_transactions)["id"] == 895315941


def test_transaction_descriptions(adv_transactions_list):
    """Тестирование функции-генератора описаний транзакций. Использует фикстуру 'adv_transactions_list'
    из модуля 'conftest.py'"""
    transactions_descriptions = generators.transaction_descriptions(adv_transactions_list)
    assert next(transactions_descriptions) == "Перевод организации"
    assert next(transactions_descriptions) == "Перевод со счета на счет"
    assert next(transactions_descriptions) == "Перевод со счета на счет"
    assert next(transactions_descriptions) == "Перевод с карты на карту"
    assert next(transactions_descriptions) == "Перевод организации"
