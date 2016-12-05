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

### DRIVER ###
ticker = input('Enter ticker symbol: ')
data = pullJSON(ticker)
parseJSON(data)

# Plotting
plotPrices(getDates(), getHighPrices())
