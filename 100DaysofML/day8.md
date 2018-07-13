# Goals 
1. Get an idea on how to have time series "slide through" [X]
    * Use a rolling / sliding window iterator to get "sliding data"
        * https://stackoverflow.com/questions/6822725/rolling-or-sliding-window-iterator
    * Plot in Jupyter notebook using a loop
    * Plot using the matplotlib animation functionality
        * http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
   
1. Get an overview over attention mechanisms[ ]
1. Think about a reasonable baseline for the NN predictions  [X] 
    * Persistence algorithm (that sounds way too smart for being that trivial)
        * https://machinelearningmastery.com/persistence-time-series-forecasting-with-python/
    * ARIMA 
        * https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
    * I think it might be helpful to familiarize myself with the data since everything I could possibly do highly depends on me having an idea of what I'm actually modelling
        * This looks like a reasonable guideline on how to do it:
            * https://machinelearningmastery.com/time-series-forecasting-python-mini-course/
        * Those visualizations might be fun to use:
            * https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-prophet-in-python-3
            * https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-visualization-with-python-3
1. How to structure a software developement project  
    * Find resources 
    * First naive draft
 
 # Insight
 * make sure the time series is not actually a random walk!!!
    *https://towardsdatascience.com/how-not-to-use-machine-learning-for-time-series-forecasting-avoiding-the-pitfalls-19f9d7adf424
    

# Ideas
* Use Hodrick-Prescott Filter to model long term trends 
* Could particle filters be useful?
* Multivariate Time Series Forecasting - this might be super useful havin multiple stock prices
    * https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/
* Time series -> LSTM
    * https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/



