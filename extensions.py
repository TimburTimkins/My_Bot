import requests
import json
from config import keys

class APIException(Exception):
    pass

class CryptoConvertion():
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base == quote:
            raise APIException('Нельзя переводить валюту в ту же валюту')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = json.loads(r.content)[keys[quote]]

        return total_base
