import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def transaction_converting_to_rubles(transaction: Any) -> float:
    """Функция принимает на вход данные о транзакции и возвращает сумму транзакции в Российских рублях.
    Если транзакция проведена в валюте, отличной от рублей, функция обращается к внешнему API, используя ключ из
    файла с переменными окружения .env, с запросом на пересчёт суммы транзакции в рубли
    """
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    payload = {}
    headers = {"apikey": os.getenv("APILAYER_KEY")}

    response = requests.request("GET", url, headers=headers, data=payload)

    result = response.json()
    return result["result"]
