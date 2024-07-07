import json
from pathlib import Path
from src.config import ROOT_PATH


def import_transactions(filename) -> list[dict]:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            try:
                transactions = json.load(file)
                return transactions
            except json.JSONDecodeError:
                print('Ошибка чтения/декодирования файла!')
                return []
    except FileNotFoundError:
        print('Ошибка: файл не найден')
        return []


operations_filename = Path(ROOT_PATH, 'data', 'operations.json')
user_operations = import_transactions(operations_filename)

# print(operations_filename)
# print(transactions[4])
