import sys
import urllib, json
from datetime import datetime
import matplotlib.pyplot as plt
import marketPull as mp

# Command line implementation of marketPull

if(len(sys.argv) == 1):
    mp.defaultSeq()
elif(len(sys.argv) == 2):
    mp.defaultSeq(sys.argv[1])
elif(len(sys.argv) == 3):
    if(sys.argv[2] == 'open'):
        mp.defaultSeq(sys.argv[1], mp.getOpeningPrices)
    elif(sys.argv[2] == 'close'):
        mp.defaultSeq(sys.argv[1], mp.getClosingPrices)
    elif(sys.argv[2] == 'low'):
        mp.defaultSeq(sys.argv[1], mp.getLowPrices)
    elif(sys.argv[2] == 'high'):
        mp.defaultSeq(sys.argv[1], mp.getHighPrices)
    else:
        print 'ERROR: Could not find function corresponding to the second parameter: ' + sys.argv[2] + '!'
        mp.defaultSeq(sys.argv[1])
else:
    print 'ERROR: You included an improper number of parameters! Expecting 0-2 parameters. You included: ' + (len(sys.argv) - 1)
