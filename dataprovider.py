"""
author: fasc
conda: py36
licence: MIT

changelog:
-6/7/18     created
-7/7/18     request -> numpy parser
-9/7/18     daily request finished
"""
import requests
import numpy as np
import pickle


def load_api_key():
    with open("API_key.txt", "r") as f:
        data = f.read()
    return str(data)


def parser(function_attr, symbol, api_key, outputsize="full", datatype="json"):

    request_params = []

    if function_attr == "TIME_SERIES_DAILY":
        request_params.append("function=" + function_attr)
        request_params.append("symbol="+symbol)
        request_params.append("outputsize="+outputsize)
        request_params.append("datatype="+datatype)
        request_params.append("apikey="+api_key)

    return "&".join(request_params)


def main():
    print(load_api_key())
    API_KEY = load_api_key()

    search_key = parser(function_attr="TIME_SERIES_DAILY", symbol="MSFT", outputsize="compact", api_key=API_KEY)
    request = "https://www.alphavantage.co/query?" + search_key

    r = requests.get(request)

    result = r.json()
    data_key = list(result.keys())[1]

    data_dict = result[data_key]
    timestamp = list(data_dict.keys())
    pickle.dump(timestamp, open("./bin/"+"_".join(["timestamps", search_key.replace(load_api_key(), "demo"),
                                                   timestamp[-1], timestamp[0]])+".pickle", 'wb'))

    instance_dict = data_dict.values()
    data_array = []

    for ii in instance_dict:
        instance_values = [float(i) for i in list(ii.values())]
        data_array.append(instance_values)

    data_array = np.array(data_array)
    np.save("./bin/"+"_".join(["data", search_key.replace(load_api_key(), "demo"), timestamp[-1],
                               timestamp[0]]), data_array)

    """
    dataForAllDays = result['Time Series (Daily)']
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
