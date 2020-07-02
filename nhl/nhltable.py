# Current MLS Table
import sys
import requests
from bs4 import BeautifulSoup

# import urllib2
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

w,h=10,32
teamInfo = [[0 for x in range(w)] for y in range(h)]

url = "http://www.livescores.com/hockey/nhl/regular-season/?lt=1"

page  = urlopen(url)
soup = BeautifulSoup(page, "lxml")

team = soup.findAll("div", {"class":"team3"})
pts = soup.findAll("div", {"class":"pts"})

def NHLTable():

  table = []

  z = 0
  for x in range(0,32):
    teamInfo[x][0] = team[x].text
    for y in range(1, 10):
      teamInfo[x][y] = pts[z].text
      z+=1

  #Format the print
  for x in range (0, 32):
    if x == 0:
      table.append("%-*s %s" % (5, teamInfo[x][9], teamInfo[x][0]))
    if x != 0 and x < 32:
      table.append("%-*s %s" % (5, teamInfo[x][9], teamInfo[x][0]))

  return '\n'.join(table)

nhltable = NHLTable()
#print (nhltable)
