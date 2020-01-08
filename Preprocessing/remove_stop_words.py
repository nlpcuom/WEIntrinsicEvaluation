__author__ = 'kjtdi'
#encoding. word encodig
#This script can be used to remove stop words from the corpus.
#We have a predefined stop word list in "stop words.txt" file.

import codecs

f_n = codecs.open("Preprocessed/test_6_no_stop.txt", 'w', encoding='utf-8')
f_stop_words = codecs.open("stop words.txt", encoding='utf-8', errors='ignore')

print("Loaded")

stop_words = []
for line in f_stop_words:
    stop_word = line.rstrip()
    stop_words.append(stop_word)

with codecs.open("Preprocessed/test_6.txt", encoding='utf-8', errors='ignore') as f:
    text = f.read()
    i = 0
    for stop_word in stop_words:
        text = text.replace(' ' + stop_word + ' ', ' ')
        i += 1
        print(i)

    f_n.write(text)

f_n.close()