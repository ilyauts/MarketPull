![Alt text](marketPull.png?raw=true)

# MarketPull
Pull historical market data!

## Expected usage of example driver:
    python marketPullDriver.py [ticker] [priceType]

## Legend:
    ticker = ['AAPL', 'JNJ', ...] # Any valid stock ticker, capitalization agnostic
    priceType = ['open', 'close', 'low', 'high']

## Price type explanations:
    'open': price of stock at the opening bell of each day
    'close': price of stock at the closing bell of each day
    'low': lowest stock price on the day
    'high': highest stock price on the day

This will result in a graph with date vs. priceType price for your stock.
