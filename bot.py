#!/usr/bin/env python
import os
import time
import json, traceback
import config
import sqlite3
import telebot
import logging
import requests
import threading
import urllib.parse as uparse
from time import sleep
from telebot import types
from datetime import date
from datetime import datetime
from waitress import serve
from nfl.nflscores import nfl
from nhl.nhlscores import nhlscores
from nhl.nhltable import nhltable
from soccer.bundesliga_table import bundesligatable
from soccer.bundesliga_scores import bundesligascores
from soccer.epltable import t
from soccer.eplscores import n as EPLSCORES
from soccer.mlstable import mlstable
from soccer.mlscores import mlscores
from soccer.laliga_scores import laligacores
from soccer.laliga_table import laligatable
from soccer.ligueone_scores import ligueonescores
from soccer.ligueone_table import ligueonetable
from soccer.seriea_table import serieatable
from soccer.seriea_scores import serieascores
from nba.nbadaily import NSN
from nba.nbastanding import NBAStanding as NSS
from flask import Flask, request, jsonify

# new bot instance
bot = telebot.TeleBot(config.api_key)

app = Flask(__name__)

@app.route("/")
def index():
     return 'What\'s good? I am Sporty! 🤖'

def bot_polling():
    while True:
        try:
            print("Starting bot polling now. New bot instance started!")
            bot.polling(none_stop=True, interval=config.bot_interval, timeout=config.bot_timeout)
        except Exception as ex:
            print("Bot polling failed, restarting in {}sec. Error:\n{}".format(config.bot_timeout, ex))
            bot.stop_polling()
            sleep(bot_timeout)
        else:
            bot.stop_polling()
            print("Bot polling loop finished.")
            break

@bot.message_handler(commands=['start'])
def send_welcome(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('⚾ Baseball', '🏀 Basketball')
    user_markup.row('🏈 Football', '🥅 Hockey')
    user_markup.row('⚽ Soccer', 'Help')
    user_markup.row('UK News', 'US News')
    cid = m.chat.id
    line1 = 'Hello, I\'m Sporty 🤖! Press any button below to interact with me. You will love using me to get sports information.'
    msg = line1
    bot.send_message(cid, msg, reply_markup=user_markup)

# main menu
@bot.message_handler(regexp="👈 Main Menu")
def main_menu(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('⚾ Baseball', '🏀 Basketball')
    user_markup.row('🏈 Football', '🥅 Hockey')
    user_markup.row('⚽ Soccer', 'Help')
    user_markup.row('UK News', 'US News')
    cid = m.chat.id
    user_msg = 'Return to the main menu.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)

# help details
@bot.message_handler(regexp="Help")
def command_help(m):
    cid = m.chat.id
    help_text = "Sporty 🤖: Send my creator *@oxnupy* a private message if you need help with anything."
    bot.send_message(cid, help_text, parse_mode='Markdown')

# us sports news
ussportsnews = requests.get(config.ussports)
ussportsnews_text = ussportsnews.text
request = json.loads(ussportsnews_text)
ussportsnews = request['articles']

@bot.message_handler(regexp="US News")
def send_news(m):
    for item in ussportsnews:
        user_msg = (item['title'] + ": " + item['url'])
        bot.reply_to(m, user_msg)

# uk sports news
uksportsnews = requests.get(config.uksports)
uksportsnews_text = uksportsnews.text
request = json.loads(uksportsnews_text)
uksportsnews = request['articles']

@bot.message_handler(regexp="UK News")
def send_news(m):
    for item in uksportsnews:
        user_msg = (item['title'] + ": " + item['url'])
        bot.reply_to(m, user_msg)

# basketball section
@bot.message_handler(regexp="🏀 Basketball")
def send_soccer(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('🏀 NBA Scores', '🏀 NBA Injury')
    user_markup.row('🏀 East Standing', '🏀 West Standing')
    user_markup.row('👈 Main Menu')
    cid = m.chat.id
    user_msg = 'Soccer information from leagues around the world.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)

@bot.message_handler(regexp="🏀 NBA Scores")
def send_nbascores(m):
  d = date.today()
  nsn = NSN()
  RESULTS = nsn.get_before(1)
  if config.current_result != RESULTS:
    config.current_result = RESULTS
  user_msg = (str(d) + "\n" + RESULTS)
  bot.reply_to(m, user_msg)

@bot.message_handler(regexp="🏀 East Standing")
def send_nbastanding(m):
  n = NSS()
  bot.reply_to(m, n.get_standings("EAST"))

@bot.message_handler(regexp="🏀 WEST Standing")
def send_nbastanding(m):
  n = NSS()
  bot.reply_to(m, n.get_standings("WEST"))

@bot.message_handler(regexp="🏀 NBA Injury")
def send_nbainjury(m):
    k = types.InlineKeyboardMarkup()
    k.add(types.InlineKeyboardButton("🏀 See NBA Injury", url="https://www.cbssports.com/nba/injuries/"))
    user_msg = 'Keep up to date on NBA injuries with CBSSports.com\'s injury report.\n\n'
    bot.reply_to(m, user_msg, reply_markup=k)

# soccer
@bot.message_handler(regexp="⚽ Soccer")
def send_soccer(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('🏴󠁧󠁢󠁥󠁮󠁧󠁿 England', '🇫🇷 France')
    user_markup.row('🇩🇪 Germany', '🇮🇹 Italy')
    user_markup.row('🇪🇸 Spain', '🇺🇸 United States')
    user_markup.row('👈 Main Menu')
    cid = m.chat.id
    user_msg = 'Soccer information from leagues around the world.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)

@bot.message_handler(regexp="👈 Back")
def soccer_back(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('🏴󠁧󠁢󠁥󠁮󠁧󠁿 England', '🇫🇷 France')
    user_markup.row('🇩🇪 Germany', '🇮🇹 Italy')
    user_markup.row('🇪🇸 Spain', '🇺🇸 United States')
    user_markup.row('👈 Main Menu')
    cid = m.chat.id
    user_msg = 'Return to main soccer options.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)

# england section
@bot.message_handler(regexp="🏴󠁧󠁢󠁥󠁮󠁧󠁿 England")
def send_england(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('⚽ EPL Scores', '⚽ EPL Table')
    user_markup.row('👈 Back')
    cid = m.chat.id
    user_msg = 'English Premier League scores and table.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)

@bot.message_handler(regexp="⚽ EPL Scores")
def send_eplscores(m):
  d = date.today()
  user_msg = (str(d) + "\n \n" + EPLSCORES)
  bot.reply_to(m, user_msg)

@bot.message_handler(regexp="⚽ EPL Table")
def send_epltable(m):
  rank = t
  user_msg = rank
  bot.reply_to(m, user_msg)

# france section
@bot.message_handler(regexp="🇫🇷 France")
def send_france(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('⚽ Ligue 1 Scores', '⚽ Ligue 1 Table')
    user_markup.row('👈 Back')
    cid = m.chat.id
    user_msg = 'French League scores and table.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)

@bot.message_handler(regexp="⚽ Ligue 1 Scores")
def send_ligueonescores(m):
  d = date.today()
  user_msg = (str(d) + "\n \n" + ligueonescores)
  bot.reply_to(m, user_msg)

@bot.message_handler(regexp="⚽ Ligue 1 Table")
def send_ligueonetable(m):
  rank = ligueonetable
  user_msg = rank
  bot.reply_to(m, user_msg)

# germany section
@bot.message_handler(regexp="🇩🇪 Germany")
def send_germany(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('⚽ Bundesliga Scores', '⚽ Bundesliga Table')
    user_markup.row('👈 Back')
    cid = m.chat.id
    user_msg = 'Spanish League scores and table.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)

@bot.message_handler(regexp="⚽ Bundesliga Scores")
def send_bundesligascores(m):
  d = date.today()
  user_msg = (str(d) + "\n \n" + bundesligascores)
  bot.reply_to(m, user_msg)

@bot.message_handler(regexp="⚽ Bundesliga Table")
def send_bundesligatable(m):
  rank = bundesligatable
  user_msg = rank
  bot.reply_to(m, user_msg)

# italy section
@bot.message_handler(regexp="🇮🇹 Italy")
def send_italy(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('⚽ Serie A Scores', '⚽ Serie A Table')
    user_markup.row('👈 Back')
    cid = m.chat.id
    user_msg = 'Serie A scores and table.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)

@bot.message_handler(regexp="⚽ Serie A Scores")
def send_serieascores(m):
  d = date.today()
  user_msg = (str(d) + "\n \n" + serieascores)
  bot.reply_to(m, user_msg)

@bot.message_handler(regexp="⚽ Serie A Table")
def send_serieatable(m):
  rank = serieatable
  user_msg = rank
  bot.reply_to(m, user_msg)

# spain section
@bot.message_handler(regexp="🇪🇸 Spain")
def send_spain(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('⚽ La Liga Scores', '⚽ La Liga Table')
    user_markup.row('👈 Back')
    cid = m.chat.id
    user_msg = 'Spanish League scores and table.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)

@bot.message_handler(regexp="⚽ La Liga Scores")
def send_laligascores(m):
  d = date.today()
  user_msg = (str(d) + "\n \n" + laligacores)
  bot.reply_to(m, user_msg)

@bot.message_handler(regexp="⚽ La Liga Table")
def send_laligatable(m):
  rank = laligatable
  user_msg = rank
  bot.reply_to(m, user_msg)

# united states section
@bot.message_handler(regexp="🇺🇸 United States")
def send_unitedstates(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('⚽ MLS Scores', '⚽ MLS Table')
    user_markup.row('👈 Back')
    cid = m.chat.id
    user_msg = 'MLS scores and table.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)

@bot.message_handler(regexp="⚽ MLS Scores")
def send_mlscores(m):
  d = date.today()
  user_msg = (str(d) + "\n \n" + mlscores)
  bot.reply_to(m, user_msg)

@bot.message_handler(regexp="⚽ MLS Table")
def send_mlstable(m):
  rank = mlstable
  user_msg = rank
  bot.reply_to(m, user_msg)

# american football section
@bot.message_handler(regexp="🏈 Football")
def send_nfl(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('🏈 NFL Scores', '🏈 NFL Fixtures')
    user_markup.row('👈 Main Menu')
    cid = m.chat.id
    user_msg = 'American Football scores and table.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)

@bot.message_handler(regexp="🏈 NFL Scores")
def send_nflscores(m):
  g = nfl
  user_msg = 'The Kansas City Chiefs are Super Bowl Champions. 🏆🎉\n' + g
  bot.reply_to(m, user_msg)

nflt = sqlite3.connect('./data/nfl.db')
cursor = nflt.cursor()

cursor.execute('SELECT * FROM nflfixtures')
nflf = cursor.fetchall()

@bot.message_handler(regexp="🏈 NFL Fixtures")
def send_nflfixtures(m):
    for row in nflf:
        user_msg = (row[0] + row[1])
        bot.reply_to(m, user_msg)

nflt.close()

#hockey section
@bot.message_handler(regexp="🥅 Hockey")
def send_hockey(m):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('🥅 NHL Scores', '🥅 NHL Table')
    user_markup.row('👈 Main Menu')
    cid = m.chat.id
    user_msg = 'Hockey scores and table.\n\n'
    bot.send_message(cid, user_msg, reply_markup=user_markup)

@bot.message_handler(regexp="🥅 NHL Scores")
def send_nhlscores(m):
  d = date.today()
  user_msg = (str(d) + "\n \n" + nhlscores)
  bot.reply_to(m, user_msg)

@bot.message_handler(regexp="🥅 NHL Table")
def send_nhlfixtures(m):
  user_msg = nhltable
  bot.reply_to(m, user_msg)

polling_thread = threading.Thread(target=bot_polling)
polling_thread.daemon = True
polling_thread.start()

# keep main program running while bot runs threaded
if __name__ == "__main__":
    serve(app)
    while True:
        try:
            sleep(120)
        except KeyboardInterrupt:
            break
