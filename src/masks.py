def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    if card_number.isdigit() and len(card_number) == 16:
        masked_card = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
        return masked_card
    else:
        return "Некорректный номер карты!"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счёта"""
    if account_number.isdigit() and len(account_number) == 20:
        masked_account = "**" + account_number[16:]
        return masked_account
    else:
        return "Некорректный номер счёта!"
