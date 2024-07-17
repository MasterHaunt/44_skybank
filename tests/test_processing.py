from src import processing


def test_filter_by_state_executed(transactions_list):
    """Тестирование работы функции отбора транзакций по параметру <state = EXECUTED>"""
    assert processing.filter_by_state(transactions_list, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 654138412, "state": "EXECUTED", "date": "2018-03-15T09:55:02.457475"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_default(transactions_list):
    """Тестирование работы функции отбора транзакций по параметру <state = EXECUTED (по умолчанию)>"""
    assert processing.filter_by_state(transactions_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 654138412, "state": "EXECUTED", "date": "2018-03-15T09:55:02.457475"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_canceled(transactions_list):
    """Тестирование работы функции отбора транзакций по параметру <state = CANCELED>"""
    assert processing.filter_by_state(transactions_list, "CANCELED") == [
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 967312458, "state": "CANCELED", "date": "2019-06-02T22:38:17.154879"},
    ]


def test_filter_by_state_invalid(transactions_list):
    """Тестирование работы функции отбора транзакций по не валидному параметру <state = DROPPED>"""
    assert processing.filter_by_state(transactions_list, "DROPPED") == []


def test_sort_transactions_by_date_descending(transactions_list):
    """Тестирование работы функции сортировки транзакций по дате по убыванию"""
    assert processing.sort_by_date(transactions_list, descending=True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 967312458, "state": "CANCELED", "date": "2019-06-02T22:38:17.154879"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 654138412, "state": "EXECUTED", "date": "2018-03-15T09:55:02.457475"},
    ]


def test_sort_transactions_by_date_default(transactions_list):
    """Тестирование работы функции сортировки транзакций по дате по убыванию (по умолчанию)"""
    assert processing.sort_by_date(transactions_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 967312458, "state": "CANCELED", "date": "2019-06-02T22:38:17.154879"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 654138412, "state": "EXECUTED", "date": "2018-03-15T09:55:02.457475"},
    ]


def test_sort_transactions_by_date_ascending(transactions_list):
    """Тестирование работы функции сортировки транзакций по дате по возрастанию"""
    assert processing.sort_by_date(transactions_list, descending=False) == [
        {"id": 654138412, "state": "EXECUTED", "date": "2018-03-15T09:55:02.457475"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 967312458, "state": "CANCELED", "date": "2019-06-02T22:38:17.154879"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_search_in_transactions(adv_transactions_list):
    """ Тестирование работы функции поиска текста в описании транзакции"""
    assert processing.search_in_transactions(adv_transactions_list, 'с карты') == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }

    ]
    assert processing.search_in_transactions(adv_transactions_list, 'со счета') == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        }]
    assert processing.search_in_transactions(adv_transactions_list, 'конвертация') == []


def test_transactions_by_categories(adv_transactions_list):
    """Тестирование работы функции подсчёта количества транзакций по заданным категориям"""
    assert processing.transactions_by_categories(adv_transactions_list,
                                                 ["Перевод со счета на счет", "Перевод организации",
                                                  "Погашение кредита"]) == {
               "Перевод организации": 2, "Перевод со счета на счет": 2, "Погашение кредита": 0}
