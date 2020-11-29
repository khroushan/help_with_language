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
from nltk.tokenize import word_tokenize
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

##########
#  read personal known words
file_word = open('known_words.txt', mode='r')
known_words = file_word.read().split()
file_word.close()
##########
# set of words in the feed
word_list_raw = word_tokenize(news, language='swedish')
word_list_lower = [word.lower() for word in word_list_raw if word.isalpha()]
unique_words = sorted(set(word_list_lower))

new_words_list = [w for w in unique_words if w not in known_words]

# print(ut.fixed_width(news))

# news_label_new_words = ut.new_words_replace(news.lower(), new_words_list)
# print(ut.fixed_width(news_label_new_words))


news_label_new_words = ut.new_words_color(news, new_words_list)
print(ut.fixed_width(news_label_new_words))
