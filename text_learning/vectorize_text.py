#!/usr/bin/python

import os
import pickle
import re
import sys

from sklearn.feature_extraction import stop_words

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        path = os.path.join('..', path[:-1])
        print path
        email = open(path, "r")

        ### use parseOutText to extract the text from the opened email
        email_text = parseOutText(email)
        ### use str.replace() to remove any instances of the words
        ### ["sara", "shackleton", "chris", "germani"]
        email_text = email_text.replace("sara","").replace("shackleton", "").replace("chris","").replace("germani","")

        ### append the text to word_data
        word_data.append(email_text)
        ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
        if name == "sara": from_data.append(0)
        if name == "chris": from_data.append(1)

        email.close()

print "emails processed"
from_sara.close()
from_chris.close()
print(word_data[152])

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )





### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words=stop_words.ENGLISH_STOP_WORDS)
vectorizer.fit(word_data)
print(len(vectorizer.get_feature_names()))

