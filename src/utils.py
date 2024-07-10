import json
import logging

logger = logging.getLogger("utils_logs")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("./logs/utils.log", "w")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(funcName)s %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def import_transactions(filename: str) -> list[dict]:
    """Функция чтения информации о транзакциях из файла *.json. На вход принимает имя файла с данными о транзакциях, на
    выходе возвращает список словарей, десериализованных из полученного файла. Если файл с указанным именем пуст или
    отсутствует - функция вернёт [] ( пустой список )"""
    logger.info("Вызвана функция загрузки информации о транзакциях из JSON-файла")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            try:
                transactions = json.load(file)
                logger.info("Информация о  транзакциях успешно загружена")
                return list(transactions)
            except json.JSONDecodeError as jdce:
                logger.error(
                    f"Функция чтения информации о транзакциях завершилась ошибкой: {jdce}"
                )
                print("Ошибка чтения/декодирования файла!")
                return []
    except FileNotFoundError as fnfe:
        logger.error(
            f"Функция чтения информации о транзакциях завершилась ошибкой: {fnfe}"
        )
        print("Ошибка: файл не найден")
        return []
