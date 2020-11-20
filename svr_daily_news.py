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
import util as ut
####################

svr_base_api = "https://api.sr.se/api/rss/program/"
program_id = 4916 # programid = 4916 for radio sweden på lätt svenska

######################################## 
raw = ut.get_raw_feed(svr_base_api + str(program_id))
num_entries = len(raw['entries'])
print("Number of today's entries: {}\n".format(num_entries))
titles = ut.get_feed_titles(raw)
print('\n'.join(titles))

feed_num = int(input('Vilket amne är du intreserad?\n'))
print('\n\n\n')
print(titles[feed_num])
print()
news = ut.get_news(raw, feed_num)
print(ut.fixed_width(news))
ut.color_example()
