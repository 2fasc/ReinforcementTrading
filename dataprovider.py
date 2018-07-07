"""
author: fasc
conda: py36
licence: MIT

changelog:
-6/7/18     created
-7/7/18     request -> numpy parser
"""
import requests


def load_API_key():
    with open("API_key.txt", "r") as f:
        data = f.read()
    return str(data)


def parser(function, symbol, api_key, outputsize="full", datatype="json"):
    request = "https://www.alphavantage.co/query?"
    request_params = []

    if function == "TIME_SERIES_DAILY":
        request_params.append("function="+function)
        request_params.append("symbol="+symbol)
        request_params.append("outputsize="+outputsize)
        request_params.append("datatype="+datatype)
        request_params.append("apikey="+api_key)

    return request+"&".join(request_params)




def main():
    print(load_API_key())
    API_KEY = load_API_key()

    request = parser(function="TIME_SERIES_DAILY", symbol="MSFT", outputsize="compact", api_key=API_KEY)
    print(request)

    r = requests.get(request)

    result = r.json()
    data_key = list(result.keys())[1]

    data_dict = result[data_key]
    timestamp = list(data_dict.keys())

    data = data_dict.values()

    for ii in data:
        print(ii)
        print(list(ii.values()))
        print("\n")

    #dataForAllDays = result['Time Series (Daily)']

    """
    print(dataForAllDays)
    dataForSingleDate = dataForAllDays['2018-07-06']

    print(dataForSingleDate['1. open'])
    print(dataForSingleDate['2. high'])
    print(dataForSingleDate['3. low'])
    print(dataForSingleDate['4. close'])
    print(dataForSingleDate['5. volume'])
    """

if __name__ == "__main__":
    main()
