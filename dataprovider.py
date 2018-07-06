"""
author: fasc
conda: py36
licence: MIT

changelog:
-6/7/18     created
"""
import requests


def load_API_key():
    with open('API_key.txt', 'r') as f:
        data = f.read()
    return str(data)


def parser():
    pass


def main():
    print(load_API_key())
    API_KEY = load_API_key()
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=' + API_KEY)
    result = r.json()
    dataForAllDays = result['Time Series (Daily)']
    dataForSingleDate = dataForAllDays['2018-07-06']

    print(dataForSingleDate['1. open'])
    print(dataForSingleDate['2. high'])
    print(dataForSingleDate['3. low'])
    print(dataForSingleDate['4. close'])
    print(dataForSingleDate['5. volume'])


if __name__ == "__main__":
    main()
