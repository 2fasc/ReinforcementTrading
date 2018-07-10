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
import matplotlib.pyplot as plt
import datetime as dt
import pickle
import os


def load_api_key():
    with open("API_key.txt", "r") as f:
        data = f.read()
    return str(data)


def parser(function_attr, symbol, api_key, interval="60min", outputsize="full", datatype="json"):

    request_params = []

    if function_attr == "TIME_SERIES_DAILY":
        request_params.append("function=" + function_attr)
        request_params.append("symbol="+symbol)
        request_params.append("outputsize="+outputsize)
        request_params.append("datatype="+datatype)
        request_params.append("apikey="+api_key)

    if function_attr == "TIME_SERIES_INTRADAY":
        if interval in ["1min", "5min", "15min", "30min", "60min"]:
            request_params.append("function=" + function_attr)
            request_params.append("symbol=" + symbol)
            request_params.append("interval=" + interval)
            request_params.append("outputsize=" + outputsize)
            request_params.append("datatype=" + datatype)
            request_params.append("apikey=" + api_key)
        else:
            raise()

    return "&".join(request_params)


def extract_from_json(search_key, request, save_request = True):

    r = requests.get(request)
    result = r.json()
    data_key = list(result.keys())[1]

    data_dict = result[data_key]
    timestamp = list(data_dict.keys())

    instance_dict = data_dict.values()
    data_array = []

    for ii in instance_dict:
        instance_values = [float(i) for i in list(ii.values())]
        data_array.append(instance_values)

    data_array = np.array(data_array)

    if save_request:
        np.save("./bin/" + "_".join(["data", search_key.replace(load_api_key(), "demo"), timestamp[-1],
                                     timestamp[0]]), data_array)

        pickle.dump(timestamp, open("./bin/" + "_".join(["timestamps", search_key.replace(load_api_key(), "demo"),
                                                         timestamp[-1], timestamp[0]]) + ".pickle", 'wb'))

    return data_array, timestamp


def main():
    print(load_api_key())
    API_KEY = load_api_key()

    search_key = parser(function_attr="TIME_SERIES_INTRADAY", symbol="MSFT", outputsize="compact", api_key=API_KEY)
    request = "https://www.alphavantage.co/query?" + search_key


    # data_array, timestamp = extract_from_json(search_key, request)

    data_array = np.load("./bin/data_function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=compact&datatype=json&"
                         "apikey=demo_2018-02-13_2018-07-06.npy")
    timestamp = pickle.load(open("./bin/timestamps_function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=compact&"
                                 "datatype=json&apikey=demo_2018-02-13_2018-07-06.pickle", 'rb'))

    date_objects = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in timestamp]

    plt.plot(date_objects, data_array[:, 0], 'ro', label='open')
    plt.plot(date_objects, data_array[:, 1], 'bo', label='high')
    plt.plot(date_objects, data_array[:, 2], 'ko', label='low')
    plt.plot(date_objects, data_array[:, 3], 'go', label='close')
    plt.xlabel('Date')
    plt.ylabel('Stock price in Dollars')
    plt.legend()
    plt.show()

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
