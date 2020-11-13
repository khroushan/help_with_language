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

# programid = 4916 for radio sweden på lätt svenska
feed_api = "https://api.sr.se/api/rss/program/4916"

raw = feedparser.parse(feed_api)
print(raw.keys())
num_entries = len(raw['entries'])
print(num_entries)

feed_num = 4

feed_html = raw['entries'][feed_num]['content'][0]['value']
feed_title = raw['entries'][feed_num]['title']
feed_text = BeautifulSoup(feed_html, 'html.parser').get_text()

titles = [str(num)+'- '+raw['entries'][num]['title'] for num in range(num_entries)]
html_list = [raw['entries'][num]['content'][0]['value'] for num in range(num_entries)]
text_list = [BeautifulSoup(item, 'html.parser').get_text()  for item in html_list]
text_all = '\n'.join(text_list)
unique_words = set(text_all.split())
print(len(unique_words))
print(unique_words)
########## 
def list_to_print(lst: list):
    return '\n\n'.join(lst)
##########
def fixed_len_print(text: str, width:int  = 50):
    return text[:70]
########## 
    
# print(list_to_print(titles))

feed_num = int(input('Vilket amne är du intreserad?\n'))
feed_html = raw['entries'][feed_num]['content'][0]['value']
feed_text = BeautifulSoup(feed_html, 'html.parser').get_text()

##########

# print(feed_text)
