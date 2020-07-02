# Live NHL Score from Past 7 Days
import requests
from bs4 import BeautifulSoup
import re
import sys
import datetime
from time import time
import re

# import urllib2
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

def NHLScores():

        url = "http://www.livescores.com/hockey/nhl/regular-season/results/"
        page  = urlopen(url)
        soup = BeautifulSoup(page, "lxml")

        o = []
        gms = soup.findAll('div', attrs={'class':'row-gray'})

        for gm in gms:
            g = gm.getText()
            g = g.replace('FT', '\n ')
            g = g.replace('OT', '\n ')
            g = re.sub(r'\(.*\)', '', g)
            o.append(g)

        # output
        if len(o) == 0:
            return("I didn't find any score at {0}".format(url))
        else:
            return("{0}".format("\n".join(o)))

nhlscores = NHLScores()
#print(cfl)
