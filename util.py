#!/usr/bin/env python 
# A short script to help improve my swedish 
# Read news from "radio sweden på lätt svenska",
#   - tokenize the text
#   - set of unique words
#   - compare with personal dictionay
#   - if it is not included save as new words
# author: Amin Ahmadi
# date: Nov 2020
####################
import feedparser
from bs4 import BeautifulSoup

svr_base_api = "https://api.sr.se/api/rss/program/"
program_id = 4916 # programid = 4916 for radio sweden på lätt svenska

########## 
def get_raw_feed(api: str):
    return feedparser.parse(api)

########## 
def get_feed_titles(raw):
    num_entries = len(raw['entries'])
    return  ['('+str(num)+') '+raw['entries'][num]['title'] for num in range(num_entries)]

##########
def get_news(raw, feed_num=0):
    feed_html = raw['entries'][feed_num]['content'][0]['value']
    return  BeautifulSoup(feed_html, 'html.parser').get_text()

##########
# fixed-length text
def my_fixed_width(text, width:int = 70):
    """ apparently there is nice library 'textwrap' for it
    don't reinvent a wheel
    """
    words = text.split()

    fixed_width_text = ''
    new_line = ''
    for word in words:
        new_line += ' ' + word
        if len(new_line) >= width:
            fixed_width_text += new_line + '\n'
            new_line = ''
    return fixed_width_text

##########
from textwrap import fill
def fixed_width(text):
    # do that with wrapper library
    return fill(text)

##########
def new_words_replace(text, words_list):
    for word in words_list:
        text = text.replace(word, ' {'+word+'} ')
        text = text.replace(word.capitalize(), ' {'+word.capitalize()+'} ')
    return text



#################### 
# text coloring
COLORS = {
"nocolor":"\u001b[0m",
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}
##########
def new_words_color(text, words_list):
    for word in words_list:
        text = text.replace(word, COLORS["blue"] + word + COLORS["nocolor"])
        text = text.replace(word.capitalize(), COLORS["blue"] + word.capitalize()+ COLORS["nocolor"])
    return text

#You can add more colors and backgrounds to the dictionary if you like.

########## 
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
########## 
def color_example():
    print(COLORS["red"]+' red'+COLORS["white"]+' white'+ COLORS["nocolor"]+' white')
