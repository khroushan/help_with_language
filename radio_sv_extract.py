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
def fixed_width(text, width:int = 70):
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
def fixed_width_v2(text):
    # do that with wrapper library
    return text

########## 


######################################## 
raw = get_raw_feed(svr_base_api + str(program_id))
num_entries = len(raw['entries'])
print("No  of entries: {}".format(num_entries))
titles = get_feed_titles(raw)
print('\n'.join(titles))

feed_num = int(input('Vilket amne är du intreserad?\n'))
print(fixed_width(get_news(raw, feed_num)))
# feed_html = raw['entries'][feed_num]['content'][0]['value']
# feed_title = raw['entries'][feed_num]['title']
# feed_text = BeautifulSoup(feed_html, 'html.parser').get_text()

html_list = [raw['entries'][num]['content'][0]['value'] for num in range(num_entries)]
text_list = [BeautifulSoup(item, 'html.parser').get_text()  for item in html_list]
text_all = '\n'.join(text_list)
unique_words = set(text_all.split())
# print(len(unique_words))
# print(unique_words)
########## 
def list_to_print(lst: list):
    return '\n\n'.join(lst)
    
# print(list_to_print(titles))


##########



# print(fixed_length(feed_text, 60))


# TODO
# list of unique words: all unique words will be collected in this file
# list of known words: this is personalized, I specify the unique words that I already know
# print new words in different colors
