import sports

all_matches = sports.all_matches()
baseball = all_matches['baseball']

width = 20

def MLBScores():

  scores = []

  for game in baseball:
    g = game
    scores.append(g)

  # output
  if len(scores) == 0:
    return("I didn't find any score at {0}".format(url))
  else:
    return('*' * (width + 4) + "{0}".format(str(scores)) + '*' * (width + 4))

mlb = MLBScores()
mlb = mlb.replace(',', '\n')
mlb = mlb.replace('-', ' - ')
mlb = mlb.replace('[', '')
mlb = mlb.replace(']', '')
mlb = mlb.replace('Anaheim Angels', 'ANA')
mlb = mlb.replace('Arizona Diamondbacks', 'ARI')
mlb = mlb.replace('Atlanta Braves', 'ATL')
mlb = mlb.replace('Baltimore Orioles', 'BAL')
mlb = mlb.replace('Boston Red Sox', 'BOS')
mlb = mlb.replace('Boston Americans', 'BOA')
mlb = mlb.replace('Boston Braves', 'BOB')
mlb = mlb.replace('Boston Bees', 'BOB')
mlb = mlb.replace('Boston Doves', 'BOD')
mlb = mlb.replace('Boston Red Sox', 'BOR')
mlb = mlb.replace('Boston Rustlers', 'BOU')
mlb = mlb.replace('Brooklyn Dodgers', 'BKN')
mlb = mlb.replace('California Angels', 'CAL')
mlb = mlb.replace('Chicago Cubs', 'CHC')
mlb = mlb.replace('Chicago Orphans', 'CHO')
mlb = mlb.replace('Chicago Colts', 'CHI')
mlb = mlb.replace('Chicago White Sox', 'CWS')
mlb = mlb.replace('Cincinnati Reds', 'CIN')
mlb = mlb.replace('Cleveland Indians', 'CLE')
mlb = mlb.replace('Colorado Rockies', 'COL')
mlb = mlb.replace('Detroit Tigers', 'DET')
mlb = mlb.replace('Florida Marlins', 'FLA')
mlb = mlb.replace('Houston Astros', 'HOU')
mlb = mlb.replace('Kansas City Royals', 'KC')
mlb = mlb.replace('Los Angeles Angels', 'LAA')
mlb = mlb.replace('Los Angeles Dodgers', 'LAD')
mlb = mlb.replace('Los Angeles Dodgers', 'LA')
mlb = mlb.replace('Miami Marlins', 'MIA')
mlb = mlb.replace('Milwaukee Brewers', 'MIL')
mlb = mlb.replace('Minnesota Twins', 'MIN')
mlb = mlb.replace('Montreal Expos', 'MTL')
mlb = mlb.replace('New York Yankees', 'NY')
mlb = mlb.replace('New York Giants', 'NYG')
mlb = mlb.replace('New York Gothams', 'NYG')
mlb = mlb.replace('New York Mets', 'NYM')
mlb = mlb.replace('New York Yankees', 'NYY')
mlb = mlb.replace('New York Highlanders', 'NYH')
mlb = mlb.replace('Oakland Athletics', 'OAK')
mlb = mlb.replace('Philadelphia Athletics', 'PHA')
mlb = mlb.replace('Philadelphia Phillies', 'PHI')
mlb = mlb.replace('Philadelphia Quakers', 'PHI')
mlb = mlb.replace('Philadelphia Phillies', 'PHP')
mlb = mlb.replace('Philadelphia Blue Jays', 'PHB')
mlb = mlb.replace('Pittsburgh Pirates', 'PIT')
mlb = mlb.replace('Pittsburgh Alleghenys', 'PIT')
mlb = mlb.replace('San Diego Padres', 'SD')
mlb = mlb.replace('Seattle Mariners', 'SEA')
mlb = mlb.replace('Seattle Pilots', 'SEA')
mlb = mlb.replace('San Francisco Giants', 'SF')
mlb = mlb.replace('St. Louis Browns', 'SLB')
mlb = mlb.replace('St. Louis Cardinals', 'SLC')
mlb = mlb.replace('St. Louis Cardinals', 'STL')
mlb = mlb.replace('Tampa Bay Rays', 'TB')
mlb = mlb.replace('Texas Rangers', 'TEX')
mlb = mlb.replace('Toronto Blue Jays', 'TOR')
mlb = mlb.replace('Washington Senators', 'WSH')
mlb = mlb.replace('Washington Nationals', 'WSH')
#print (mlb)
