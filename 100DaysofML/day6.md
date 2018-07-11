# Goal 
1. [ ] read http://www.wildml.com/2018/02/introduction-to-learning-to-trade-with-reinforcement-learning/ since this seems to be pretty much the same idea
2. [x] read http://www.wildml.com/2016/10/learning-reinforcement-learning/

# Insights
* This is the most commonly referenced RL course http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html 
* Sutton Barto seems to be the go to book in the field

* The volume of trade is 
  a) an indicator for how liquid the market is 
  b) an indicator for how reliable a trend is (consensus of market participants)

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
