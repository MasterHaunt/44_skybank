from src import masks


def mask_account_card(account_card: str) -> str:
    """Функция маскировки номера карты/счёта"""

    # Если первые пять символов - "Счет" -> на входе номер счёта, применяем функцию маскировки номера счёта
    if account_card[0:4] == "Счет":
        account_id = "Счет " + masks.get_mask_account(account_card[-20:])
        return account_id

    # Если первые пять символов - не "Счет" -> на входе номер карты, применяем функцию маскировки номера карты
    else:
        card_id = account_card[0:-16] + masks.get_mask_card_number(account_card[-16:])
        return card_id


def transaction_date(transaction_datetime: str) -> str:
    """функция определения даты транзакции"""
    return transaction_datetime[8:10] + "." + transaction_datetime[5:7] + "." + transaction_datetime[0:4]
