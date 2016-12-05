import urllib, json
from datetime import datetime
import matplotlib.pyplot as plt

dates = []
openingPrices = []
closingPrices = []
lowPrices = []
highPrices = []

def pullJSON(ticker):
    url = "https://www.quandl.com/api/v3/datasets/WIKI/" + ticker + ".json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

# organize the json into nice date-time maps
def parseJSON(data):
    prices = data['dataset']['data'];
    for i in range(0, len(prices)):
        currPrices = prices[i]
        dates.append(datetime.strptime(currPrices[0], '%Y-%m-%d'))
        openingPrices.append(currPrices[1])
        closingPrices.append(currPrices[4])
        lowPrices.append(currPrices[3])
        highPrices.append(currPrices[2])

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

### DRIVER ###
ticker = input('Enter ticker symbol: ')
data = pullJSON(ticker)
parseJSON(data)

# Plotting
plotPrices(getDates(), getClosingPrices())
