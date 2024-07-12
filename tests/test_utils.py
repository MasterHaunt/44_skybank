import json
import pandas as pd
from unittest.mock import Mock

from src.utils import import_json_transactions
from src.utils import import_xlsx_transactions
from src.utils import import_csv_transactions


def test_import_json_transactions():
    """Тестирование функции десериализации данных о транзакциях из файла *.json. Вместо функции загрузки информации о
    транзакциях, которая мспользуется в тестируемой функции, подставлен объект Mock, возвращающий данные об одной
    транзакции в требуемом виде"""
    mock_transaction = Mock(
        return_value=[
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        ]
    )
    json.load = mock_transaction
    assert import_json_transactions("./data/operations.json") == [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    ]
    mock_transaction.assert_called_once()


def test_import_xlsx_transactions():
    """Тестирование функции чтения информации о транзакциях из файла *.xlsx
    проверяется соответствие параметров 'shape' и 'columns' полученного датафрейма, а также проверка возврата функцией
    import_xlsx_transactions пустого значения (None), если файл с информацией о транзакциях не найден"""
    assert import_xlsx_transactions("./data/transactions_excel.xlsx").shape == (1000, 9)
    assert (
        pd.DataFrame(import_xlsx_transactions("./data/transactions_excel.xlsx").columns).index.all()
        == pd.DataFrame(
            [
                "id",
                "state",
                "date",
                "amount",
                "currency_name",
                "currency_code",
                "from",
                "to",
                "description",
            ],
            dtype="object",
        ).index.all()
    )
    assert str(import_xlsx_transactions("./data/None_transactions_excel.xlsx")) == "None"


def test_import_csv_transactions():
    """Тестирование функции чтения информации о транзакциях из файла *.csv
    проверяется соответствие параметров 'shape' и 'columns' полученного датафрейма, а также проверка возврата функцией
    import_csv_transactions пустого значения (None), если файл с информацией о транзакциях не найден"""
    assert import_csv_transactions("./data/transactions.csv").shape == (1000, 9)
    assert (
        pd.DataFrame(import_csv_transactions("./data/transactions.csv").columns).index.all()
        == pd.DataFrame(
            [
                "id",
                "state",
                "date",
                "amount",
                "currency_name",
                "currency_code",
                "from",
                "to",
                "description",
            ],
            dtype="object",
        ).index.all()
    )
    assert str(import_csv_transactions("./data/None_transactions.csv")) == "None"
