# Goal 
1. [x] read http://www.wildml.com/2018/02/introduction-to-learning-to-trade-with-reinforcement-learning/ since this seems to be pretty much the same idea
2. [x] read http://www.wildml.com/2016/10/learning-reinforcement-learning/

# Insights
* This is the most commonly referenced RL course http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html 
* Sutton Barto seems to be the go to book in the field

* The volume of trade is 
  a) an indicator for how liquid the market is 
  b) an indicator for how reliable a trend is (consensus of market participants)

* The timescale defines the strategy used
  * Holding longterm assets is like a bet that something will be successful -> News, key insights ...
    * Long Term Reasoning is not in the scope of this project and an ongoing field of research
  * High Frequency Trading (HFT) is simple but super fast pattern matching with FPGAs
    * Neural networks are too slow to operate on the nano sec timescales involved here

* Training an RL agent we'll have to decide wether we rather want frequent feedback or longer term strategies - depending on the choosen reward function (trades as reward are relatively sparse compared to doing nothing)

* The reward function will be a tradeoff between profit maximization and risk avoidance. 

* Learned policy is only optimal for certain market conditions
  * Is it possible to gain robustness by training an ensemble?
    
** In order to create a somewhat meaningful algorithm it has to compete somewhere between the two extremes:
faster than any human could but with more insight than a simple FPGA tool - Ideally  that would be in the ms-min
range but the finest data available is in a minute interval. I guess minutes it is.**

# Simplifications
* Buy and sell at the same level
* Assume the market is always perfectly liquid (you can trade always at whichever volume)
  * usually it depends on the current trade volume (don't @ me I know this is simplified)
* Assume that placing buy or sell orders doesn't affect the market in price level or liquidity
* Assume that a market order can be satisfied at the lowest price level
* Start with market orders (buy or sell now for the current price)
* No latency in the network

# Things to consider
* There is a taker fee (0-0.3%) when you place a market order 
* Cap max trading volume in order to not break the assumptions (5 million dollars would consume the whole volume at the lowwest price level)
* If a supervised model is used: How to deal with uncertainty in the prediction? How can they be modeled in a regression?
* limit orders (if the price reaches a certain level buy or sell)
* Which metric do I want to optimize for? (sure profit but there is more to that)
  * Net PnL (Net Profit and Loss)
  * Alpha and Beta
  * Sharpe Ratio
  * Maximum Drawdown
  * VaR
 * Is it possible to model multiple prices in one model an thus use correlations for your prediction?
