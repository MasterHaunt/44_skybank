def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает на вход список словарей с информацией о транзакциях и возвращает список словарей с информацией
    о транзакциях, которые были исполнены ("state" = "EXECUTED"). Если помимо списка словарей в функцию передан второй
    параметр в значении "CANCELED" - возвращается список словарей с информацией об отменённых транзакциях"""

    filtered_transactions = []
    for transaction in transactions:
        if transaction["state"] == state:
            filtered_transactions.append(transaction)
    return filtered_transactions


def sort_by_date(transactions: list[dict], *, descending: bool = True) -> list[dict]:
    """Функция принимает на вход список словарей с информацией о транзакциях и возвращает его отсортированным:
    - если второй параметр не передан или передан в значении "True" -> по убыванию (от ранних к поздним);
    - если второй параметр передан в значении "False" -> по возрастанию (от последних к ранним)"""

    return sorted(transactions, key=lambda transaction: transaction["date"], reverse=descending)
