import os
from dotenv import load_dotenv
from typing import Any
import requests

load_dotenv()

api_key = os.getenv("APILAYER_KEY")


# print(api_key)
def transaction_converting_to_rubles(transaction: Any) -> float:
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    payload = {}
    headers = {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # status_code = response.status_code
    result = response.json()
    return result["result"]

# example_transaction = {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }
#
# print(transaction_converting_to_rubles(example_transaction))
