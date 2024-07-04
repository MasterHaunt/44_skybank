import pytest

from src import masks


@pytest.mark.parametrize(
    "card_number, masked_card_number",
    [
        ("4200568974529687", "4200 56** **** 9687"),
        ("420O568974529687", "Некорректный номер карты!"),
        ("420056897452687", "Некорректный номер карты!"),
        ("42005689745268700", "Некорректный номер карты!"),
    ],
    ids=[
        "correct card number",
        "card number not numeric",
        "length is shorter then expected",
        "length is longer then expected",
    ],
)
def test_get_mask_card_number(card_number, masked_card_number):
    """Тестирование работы функции маскировки номера банковской карты"""
    assert masks.get_mask_card_number(card_number) == masked_card_number


@pytest.mark.parametrize(
    "account_number, masked_account_number",
    [
        ("73654108430135874305", "**4305"),
        ("130208758470O0165874", "Некорректный номер счёта!"),
        ("1302087584700165874", "Некорректный номер счёта!"),
    ],
)
def test_get_mask_account(account_number, masked_account_number):
    """Тестирование работы функции маскировки номера банковского счёта"""
    assert masks.get_mask_account(account_number) == masked_account_number
