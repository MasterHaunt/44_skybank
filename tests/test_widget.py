import pytest

from src import widget


@pytest.mark.parametrize(
    "transaction_datetime, transaction_date",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-03-15T09:55:02.457475", "15.03.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
        ("2019-06-02T22:38:17.154879", "02.06.2019"),
    ],
)
def test_transaction_date(transaction_datetime, transaction_date):
    """Функция тестирования корректности преобразования времени проведения транзакции в дату формата <ДД.ММ.ГГГГ>"""
    assert widget.transaction_date(transaction_datetime) == transaction_date


@pytest.mark.parametrize(
    "account_card_number, masked_account_card_number",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_mask_account_card(account_card_number, masked_account_card_number):
    """Функция тестирования корректности маскировки номера банковского счёта/банковской карты"""
    assert widget.mask_account_card(account_card_number) == masked_account_card_number
