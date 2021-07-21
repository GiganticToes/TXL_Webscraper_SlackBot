import pandas as pd
import requests
from time import sleep

NOMICS_APIKEY = '34fbeb63bb635510a00eb6c8ee108c8b97d2be7e'


def get_txl(fiat='AUD', ticker='BTC'):
    url = 'https://api.nomics.com/v1/currencies/ticker'
    payload = {'key': NOMICS_APIKEY, 'convert': fiat,
               'ids': ticker, 'interval': '1d'}
    response = requests.get(url, params=payload)
    data = response.json()

    price, timestamp = [], []

    print("Data is: ")
    print(data)


get_txl()
