import logging

logger = logging.getLogger("masks_logs")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("./logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(funcName)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info(f"Вызвана функция маскирования номера банковской карты: {card_number}")
    if card_number.isdigit() and len(card_number) == 16:
        masked_card = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
        logger.info(f"Номер карты замаскирован: {masked_card}")
        return masked_card
    else:
        logger.error(f"Функция маскирования номера карты завершилась ошибкой: Некорректный номер карты: {card_number}")
        return "Некорректный номер карты!"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счёта"""
    logger.info(f"Вызвана функция маскирования номера банковского счёта: {account_number}")
    if account_number.isdigit() and len(account_number) == 20:
        masked_account = "**" + account_number[16:]
        logger.info(f"Номер банковского счёта замаскирован: {masked_account}")
        return masked_account
    else:
        logger.error(
            f"Функция маскирования номера счёта завершилась ошибкой: Некорректный номер счёта: {account_number}"
        )
        return "Некорректный номер счёта!"
