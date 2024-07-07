import json
from unittest.mock import Mock

from src.utils import import_transactions


def test_import_transactions():
    """Тестирование функции десериализации данных о транзакциях из файла *.json. Вместо функции загрузки информации о
    транзакциях, которая мспользуется в тестируемой функции, подставлен объект Mock, возвращающий данные об одной
    транзакции в требуемом виде"""
    mock_transaction = Mock(
        return_value={
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
    )
    json.load = mock_transaction
    assert import_transactions("./data/operations.json") == {
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
    mock_transaction.assert_called_once()
