from collections import Counter
import re


def filter_by_state(transactions: list[dict], s_state: str = "EXECUTED") -> list[dict]:
    """Функция принимает на вход список словарей с информацией о транзакциях и возвращает список словарей с информацией
    о транзакциях, которые были исполнены ("state" = "EXECUTED"). Если помимо списка словарей в функцию передан второй
    параметр в значении "CANCELED" - возвращается список словарей с информацией об отменённых транзакциях
    """

    filtered_transactions = []
    for transaction in transactions:

        if transaction.get('state') == s_state:
            filtered_transactions.append(transaction)
    return filtered_transactions


def sort_by_date(transactions: list[dict], *, descending: bool = True) -> list[dict]:
    """Функция принимает на вход список словарей с информацией о транзакциях и возвращает его отсортированным:
    - если второй параметр не передан или передан в значении "True" -> по убыванию (от ранних к поздним);
    - если второй параметр передан в значении "False" -> по возрастанию (от последних к ранним)
    """

    return sorted(
        transactions, key=lambda transaction: transaction["date"], reverse=descending
    )


def search_in_transactions(transactions: list[dict], query: str) -> list[dict]:
    """Функция принимает на вход список словарей с информацией о транзакциях и текстовую строку для поиска, а
    возвращает список словарей с информацией о тех транзакциях, в описании (поле 'description') которых присутствует
    текст из строки для поиска
    """

    queried_transactions = []
    for transaction in transactions:
        if re.search(query, transaction["description"], flags=re.IGNORECASE):
            queried_transactions.append(transaction)
    return queried_transactions


def transactions_by_categories(transactions: list[dict], categories: list[str]) -> dict:
    """Функция принимает на вход список словарей с информацией о транзакциях и список с названиями категорий операций,
     а возвращает словарь, в котором ключи - наименования категорий операций, а значения - количества операций
     соответствующих категорий
    """

    result_list = []
    for category in categories:
        # result_dict[category] = 0
        for transaction in transactions:
            if transaction["description"] == category:
                result_list.append(category)
    counted = Counter(result_list)
    for category in categories:
        if category not in counted.keys():
            counted[category] = 0
    return counted


def transactions_by_currency(transactions: list[dict], currency: str) -> list[dict]:
    """Функция принимает на вход список словарей 'transactions' с информацией о транзакциях и код валюты
    'currency', по которому должна проводиться фильтрация. При каждом вызове функция возвращает словарь с информацией
    о транзакции, проведённой в валюте, указанной в параметре 'currency'"""
    filtered_transactions = []
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            filtered_transactions.append(transaction)
    return filtered_transactions
