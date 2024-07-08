import json


def import_transactions(filename: str) -> list[dict]:
    """Функция чтения информации о транзакциях из файла *.json. На вход принимает имя файла с данными о транзакциях, на
    выходе возвращает список словарей, десериализованных из полученного файла. Если файл с указанным именем пуст или
    отсутствует - функция вернёт [] ( пустой список )"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            try:
                transactions = json.load(file)
                return transactions
            except json.JSONDecodeError:
                print("Ошибка чтения/декодирования файла!")
                return []
    except FileNotFoundError:
        print("Ошибка: файл не найден")
        return []
