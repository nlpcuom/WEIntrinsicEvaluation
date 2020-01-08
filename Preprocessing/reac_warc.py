__author__ = 'kjtdi'

import codecs
from bs4 import BeautifulSoup

import re

def remove_warc_content(line):
    start_with_prefixes = ['WARC','Content-Type','Content-Length','Keep-Alive','X-Crawler', 'HTTP/1.1']
    for prefix in start_with_prefixes:
        if(line.startswith(prefix)):
            return True

    return False

def strip_html(text):
    soup = BeautifulSoup(text) # create a new bs4 object from the html data loaded
    for script in soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def remove_comments(line, sep):
    for s in sep:
        i = line.find(s)
        if i >= 0:
            line = line[:i]
    return line.strip()

def remove_special_chars(text):
   return  re.sub('[\W\_]','',text)


def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = remove_comments(text, '#')

    return text


i=0

f = codecs.open("D:/NLP/Corpus/commoncrawl.deduped.si", encoding='utf-8', errors='ignore')
f_w = codecs.open("test.txt", 'w', 'utf-8')

lines = ""
for line in f:
    if(not remove_warc_content(line)):
        lines += str(line)

    print(i)
    i = i+1
    if(i>10000):
        break

# noise_removed_text = denoise_text(lines)
f_w.write(lines)

f_w.close()