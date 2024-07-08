from unittest.mock import patch

from src.external_api import transaction_converting_to_rubles


@patch("requests.get")
def test_transaction_converting_to_rubles(mock_get):
    """Тестирование функции конвертации суммы транзакции в рубли при помощи декоратора @patch"""
    mock_get.return_value.json.return_value = {"result": "1000.00"}
    assert (
        transaction_converting_to_rubles(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "1000.00",
                    "currency": {"name": "руб.", "code": "RUB"},
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == "1000.00"
    )
