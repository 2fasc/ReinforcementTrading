# Goals 
>> “Give me six hours to chop down a tree and I will spend the first four sharpening the axe.”
>> ― Abraham Lincoln 
1. Get an idea on how to have time series "slide through" [X]
    * Use a rolling / sliding window iterator to get "sliding data"
        * https://stackoverflow.com/questions/6822725/rolling-or-sliding-window-iterator
    * Plot in Jupyter notebook using a loop
    * Plot using the matplotlib animation functionality
        * http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
   
1. Get an overview over attention mechanisms [x]
    * http://www.wildml.com/2016/01/attention-and-memory-in-deep-learning-and-nlp/
    * https://machinelearningmastery.com/attention-long-short-term-memory-recurrent-neural-networks/
    * https://machinelearningmastery.com/global-attention-for-encoder-decoder-recurrent-neural-networks/
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
1. How to structure a software developement project [x]
    * Find resources 
        * Scrum is a framework that a) suits my style of working b) is currently hyped in the private sector
            * https://en.wikipedia.org/wiki/Scrum_%28software_development%29
        * Scrum Planning
            * http://scrumprimer.org/scrumprimer20.pdf
        * Scrum Planning example
            * https://platinumedge.com/sites/default/files/public/Sprint-Planning-Checklist-Platinum-Edge.pdf
        * Scrum templates
            * https://codehollow.com/scrum-meeting-templates/
        * Pretty old but has reasonable explanations - standard:
            * http://se.inf.ethz.ch/old/teaching/ws2005/0273/slides/Template%20Project%20Plan.pdf
        * Also quite old but looks like a good exampl - standard:        
            * [https://www.utdallas.edu/chung/RE/Presentations10F/Team-hope/5%20-%20Project%20Plan.pdf](https://www.utdallas.edu/~chung/RE/Presentations10F/Team-hope/5%20-%20Project%20Plan.pdf)             
    
1. How to manage results of experiments efficiently [ ]
    * Spreadsheet
        * https://machinelearningmastery.com/plan-run-machine-learning-experiments-systematically/
    * Python to GoogleDocs
        * https://www.youtube.com/watch?v=7I2s81TsCnc
        * https://www.youtube.com/watch?v=nB6TPfcVKSo
    
    
 
 # Insight
 * make sure the time series is not actually a random walk!!!
    * https://towardsdatascience.com/how-not-to-use-machine-learning-for-time-series-forecasting-avoiding-the-pitfalls-19f9d7adf424
 
 * Attention mechanisms are usually applied to sequence to sequence problems. That was not what I was going for but... why not predict a sequence of future prices?
    * also https://arxiv.org/abs/1406.6247 looks super interesting - building non-differentiable models and training them with RL sounds like a new idea to me (well kinda I also saw a repo where somebody used genetic algorithms)
    
 * It might be super helpful to have a template to plan 2 week sprints in advance and structure the whole process without annoying myself. 
 Nonetheless, thinking through the bigger picture (even if that changes over time) seems to be utterly important in order to avoid 
 ending up at dead ends or encountering foreseeable and avoidable problems. Strip down principles to their core since unnecessary overhead will cause me to abandon this
 concept. 
 
 * It seems like there is no good or widely used solution. I think spreadsheets are usefull but it might be tedious to maintain them - 
 I heard about ways to access google docs from python - how about creating a tool to write spreadsheets automatically?
# Ideas
* Use Hodrick-Prescott Filter to model long term trends 
* Could particle filters be useful?
* Multivariate Time Series Forecasting - this might be super useful havin multiple stock prices
    * https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/
* Time series -> LSTM
    * https://machinelearningmastery.com/reshape-input-data-long-short-term-memory-networks-keras/



