import sys
import urllib, json
from datetime import datetime
import matplotlib.pyplot as plt

dates = []
openingPrices = []
closingPrices = []
lowPrices = []
highPrices = []

# Indices
dateIndex = 0
openingIndex = 1
closingIndex = 4
lowIndex = 3
highIndex = 2
splitIndex = 7

# Get json file with ticker data
def pullJSON(ticker):
    url = "https://www.quandl.com/api/v3/datasets/WIKI/" + ticker + ".json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

# Organize the json into nice date-time maps
def parseJSON(data):
    prices = data['dataset']['data'];

    splitMultiplier = 1

    # Adjust for splits
    for i in range(0, len(prices)):
        currPrices = prices[i]

        dates.append(datetime.strptime(currPrices[dateIndex], '%Y-%m-%d'))
        openingPrices.append(currPrices[openingIndex] / splitMultiplier)
        closingPrices.append(currPrices[closingIndex] / splitMultiplier)
        lowPrices.append(currPrices[lowIndex] / splitMultiplier)
        highPrices.append(currPrices[highIndex] / splitMultiplier)

        splitMultiplier = splitMultiplier * currPrices[splitIndex]

# Getters
def getDates():
    return dates

def getOpeningPrices():
    return openingPrices

def getClosingPrices():
    return closingPrices

def getLowPrices():
    return lowPrices

def getHighPrices():
    return highPrices

def plotPrices(xVals, yVals):
    plt.scatter(xVals,yVals)
    plt.show()

# Default sequence - if all else fails go here
def defaultSeq(ticker = 'AAPL', functionCall = getHighPrices):
    data = pullJSON(ticker)
    parseJSON(data)

    # Plotting
    plotPrices(getDates(), functionCall())

'''
## DRIVER ##

Expected usage:
    python marketPull.py [ticker] [priceType]

Legend:
-------
    ticker = ['AAPL', 'JNJ', ...] # Any valid stock ticker, capitalization agnostic
    priceType = ['open', 'close', 'low', 'high']
'''

if(len(sys.argv) == 1):
    defaultSeq()
elif(len(sys.argv) == 2):
    defaultSeq(sys.argv[1])
elif(len(sys.argv) == 3):
    if(sys.argv[2] == 'open'):
        defaultSeq(sys.argv[1], getOpeningPrices)
    elif(sys.argv[2] == 'close'):
        defaultSeq(sys.argv[1], getClosingPrices)
    elif(sys.argv[2] == 'low'):
        defaultSeq(sys.argv[1], getLowPrices)
    elif(sys.argv[2] == 'high'):
        defaultSeq(sys.argv[1], getHighPrices)
    else:
        print 'ERROR: Could not find function corresponding to the second parameter: ' + sys.argv[2] + '!'
        defaultSeq(sys.argv[1])
else:
    print 'ERROR: You included an improper number of parameters! Expecting 0-2 parameters. You included: ' + (len(sys.argv) - 1)
