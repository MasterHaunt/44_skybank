import json
import logging
import pandas as pd
from typing import Any

logger = logging.getLogger("utils_logs")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("./logs/utils.log", "w")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(funcName)s %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def import_json_transactions(filename: str) -> list[dict]:
    """Функция чтения информации о транзакциях из файла *.json. На вход принимает имя файла с данными о транзакциях, на
    выходе возвращает список словарей, десериализованных из полученного файла. Если файл с указанным именем пуст или
    отсутствует - функция вернёт [] ( пустой список )"""
    logger.info("Вызвана функция загрузки информации о транзакциях из JSON-файла")
    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            try:
                transactions = json.load(json_file)
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


def import_xlsx_transactions(xlsx_filename: str) -> Any:
    """Функция чтения информации о транзакциях из файла *.xlsx. На вход принимает имя файла с данными о транзакциях, на
    выходе возвращает датафрейм. Если файл с указанным именем пуст или отсутствует - функция вернёт [] ( пустой
    список )"""
    logger.info("Вызвана функция загрузки информации о транзакциях из XLSX-файла")
    try:
        # with open(xlsx_filename, "r") as xlsx_file:
            try:
                xlsx_transactions = pd.read_excel(xlsx_filename)
                if xlsx_transactions.empty:
                    logger.error("В указанном XLSX-файле информация отсутствует!")
                    print("В указанном XLSX-файле информация отсутствует!")
                    return []
                else:
                    logger.info("Информация о транзакциях успешно загружена")
                    return xlsx_transactions
            except Exception as e:
                logger.error(f"Функция чтения информации о транзакциях из XLSX-файла завершилась ошибкой: {e}")
                print("Ошибка чтения/декодирования файла!")
                return []
    except FileNotFoundError as fnfe:
        logger.error(
            f"Функция чтения информации о транзакциях завершилась ошибкой: {fnfe}"
        )
        print("Ошибка: файл не найден")
        return []
