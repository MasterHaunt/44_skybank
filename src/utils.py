import json
import logging
import pandas as pd
from pandas import DataFrame

logger = logging.getLogger("utils_logs")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("./logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(funcName)s %(levelname)s: %(message)s")
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
                logger.error(f"Функция чтения информации о транзакциях завершилась ошибкой: {jdce}")
                print("Ошибка чтения/декодирования файла!")
                return []
    except FileNotFoundError as fnfe:
        logger.error(f"Функция чтения информации о транзакциях завершилась ошибкой: {fnfe}")
        print("Ошибка: файл не найден")
        return []


def import_xlsx_transactions(xlsx_filename: str) -> DataFrame | DataFrame | None:
    """Функция чтения информации о транзакциях из файла *.xlsx. На вход принимает имя файла с данными о транзакциях, на
    выходе возвращает датафрейм. Если файл с указанным именем пуст или отсутствует - функция вернёт [] ( пустой
    список )"""
    logger.info("Вызвана функция загрузки информации о транзакциях из XLSX-файла")
    try:
        try:
            xlsx_transactions = pd.read_excel(xlsx_filename)
            if xlsx_transactions.empty:
                logger.error("В указанном XLSX-файле информация отсутствует!")
                print("В указанном XLSX-файле информация отсутствует!")
                return None
            else:
                logger.info("Информация о транзакциях успешно загружена")
                return xlsx_transactions
        except Exception as e:
            logger.error(f"Функция чтения информации о транзакциях из XLSX-файла завершилась ошибкой: {e}")
            print("Ошибка чтения/декодирования файла!")
            return None
    except FileNotFoundError as fnfe:
        logger.error(f"Функция чтения информации о транзакциях завершилась ошибкой: {fnfe}")
        print("Ошибка: файл не найден")
        return None


def import_csv_transactions(csv_filename: str) -> None | DataFrame | DataFrame:
    """Функция чтения информации о транзакциях из файла *.csv. На вход принимает имя файла с данными о транзакциях, на
    выходе возвращает датафрейм. Если файл с указанным именем пуст или отсутствует - функция вернёт [] ( пустой
    список )"""
    logger.info("Вызвана функция загрузки информации о транзакциях из CSV-файла")
    try:
        try:
            csv_transactions = pd.read_csv(csv_filename, delimiter=";")
            if csv_transactions.empty:
                logger.error("В указанном CSV-файле информация отсутствует!")
                print("В указанном CSV-файле информация отсутствует!")
                return None
            else:
                logger.info("Информация о транзакциях успешно загружена")
                return csv_transactions
        except Exception as e:
            logger.error(f"Функция чтения информации о транзакциях из CSV-файла завершилась ошибкой: {e}")
            print("Ошибка чтения/декодирования файла!")
            return None
    except FileNotFoundError as fnfe:
        logger.error(f"Функция чтения информации о транзакциях завершилась ошибкой: {fnfe}")
        print("Ошибка: файл не найден")
        return None


def df_string_to_dict(input_string: pd.Series) -> dict:
    """Функция преобразует строку датафрейма с информацией о транзакции в словарь заданного формата
    Если поле "id" не содержит символ "."(признак вещественного числа), то создаётся пустой словарь  для последующего
    исключения из итогового списка"""
    if str(input_string["id"]).__contains__("."):
        result_dict = {
            "id": input_string["id"],
            "state": input_string["state"],
            "date": input_string["date"],
            "operationAmount": {
                "amount": input_string["amount"],
                "currency": {"name": input_string["currency_name"], "code": input_string["currency_code"]},
            },
            "description": input_string["description"],
            "from": input_string["from"],
            "to": input_string["to"],
        }
    else:
        result_dict = {}
    return result_dict


def dataframe_to_list_of_dicts(input_dataframe: DataFrame) -> list[dict]:
    """Функция принимает на вход датафрейм с информацией о транзакциях, преобразует каждую строку датафрейма функцией
    df_string_to_dict, затем собирает преобразованные строки в список словарей.
    Пустой словарь в список не добавляется"""
    result_list = []

    transactions = input_dataframe.apply(df_string_to_dict, axis=1)

    for df_row in transactions:
        if df_row != {}:
            df_row["id"] = int((str(df_row["id"])[0:-2]))
            result_list.append(df_row)
    return result_list
