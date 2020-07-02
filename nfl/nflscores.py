#Live NFL Scores
import xml.etree.ElementTree as ET
import requests

#http://www.nfl.com/ajax/scorestrip?season=2019&seasonType=REG&week=16
#http://www.nfl.com/liveupdate/scorestrip/ss.xml
#Type will be PRE, REG, PRO or POST.
#Week is 0-4 for PRE, 1-17 for REG, 21 for PRO and 18-20 & 22 for POST
x = requests.get("http://www.nfl.com/ajax/scorestrip?season=2019&seasonType=POST&week=22")
tree = ET.fromstring(x.text)
gms = tree[0]

ret = ''

for g in gms:
    ret = ret + "\n  {:<2} [Home] - [Away] {:<2} Score: {:<2} - {:<2}".format(g.attrib['hnn'].capitalize(), g.attrib['vnn'].capitalize() + "\n ", g.attrib['hs'], g.attrib['vs']) + "\n"
    if g.attrib['q'] == "F":
        ret = ret + "  Game Status: Final" + "\n "
    elif g.attrib['q'] == "FO":
        ret = ret + "  Game Status: Final [Overtime]" + "\n"
    elif g.attrib['q'] == 'H':
        ret = ret + "  Game Status: Haftime" + "\n"
    elif g.attrib['q'] == '1' or g.attrib['q'] == '2' or g.attrib['q'] == '3' or g.attrib['q'] == '4':
        ret = ret + " quarter: {} - {}".format(g.attrib['q'], g.attrib['k'])
    else:
        ret = ret + " quarter: {}".format(g.attrib['q'])
ret = ret

def nfl():
    return (ret)

nfl = nfl()
#print (nfl)