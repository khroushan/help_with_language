#!/usr/bin/env python 

# A short script to help improve my swedish 
# Read news from "radio sweden på lätt svenska",
#   - tokenize the text
#   - set of unique words
#   - compare with personal dictionay
#   - if it is not included save as new words

#################### 
# author: Amin Ahmadi
# date: Nov 2020
####################
import feedparser
from bs4 import BeautifulSoup
import util as ut
from nltk.tokenize import word_tokenize
####################

# API inputs
svr_base_api = "https://api.sr.se/api/rss/program/"
program_id = 4916 # programid = 4916 for radio sweden på lätt svenska

#################### 
# read feed and titles
raw = ut.get_raw_feed(svr_base_api + str(program_id))
num_entries = len(raw['entries'])
print("Number of today's entries: {}\n".format(num_entries))
titles = ut.get_feed_titles(raw)
print("\n Today's first title:{}".format(titles[0]))

#################### 
# get the news' text
html_list = [raw['entries'][num]['content'][0]['value'] for num in range(num_entries)]
text_list = [BeautifulSoup(item, 'html.parser').get_text()  for item in html_list]
text_all = '\n'.join(text_list)

#################### 
# contruct unique words of the text
# numbers and non-words are removed
word_list_raw = word_tokenize(text_all, language='swedish')
word_list_lower = [word.lower() for word in word_list_raw if word.isalpha()]
unique_words = sorted(set(word_list_lower))

####################
# update unique words file

file_word = open('list_of_words.txt', mode='r')
words = file_word.read().split()
file_word.close()
word_list_length_pre = len(words)
# add previous words
unique_words += words
# unique words again
unique_words = sorted(set(unique_words))
word_list_length_after = len(unique_words)
word_to_write = '\n'.join(unique_words)
# update the file
file_word = open('list_of_words.txt', mode='w')
file_word.write(word_to_write)
file_word.close()

print("number of accumulated unique words before: {} and after: {}"
      .format(word_list_length_pre, word_list_length_after))
