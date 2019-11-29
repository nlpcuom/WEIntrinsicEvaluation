from __future__ import absolute_import, division, print_function

from sinling.sinhala.tokenizer import SinhalaTweetTokenizer

#encoding. word encodig
import codecs
#finds all pathnames matching a pattern, like regex
#concurrency
import multiprocessing
#dealing with operating system , like reading file
import os
import pickle

import gensim.models.fasttext as fasttext
from gensim.test.utils import get_tmpfile

f_1 = codecs.open("Preprocessed/test_1_no_stop.txt", encoding='utf-8', errors='ignore')
f_2 = codecs.open("Preprocessed/test_2_no_stop.txt", encoding='utf-8', errors='ignore')
f_3 = codecs.open("Preprocessed/test_3_no_stop.txt", encoding='utf-8', errors='ignore')
f_4 = codecs.open("Preprocessed/test_4_no_stop.txt", encoding='utf-8', errors='ignore')
f_5 = codecs.open("Preprocessed/test_5_no_stop.txt", encoding='utf-8', errors='ignore')
f_6 = codecs.open("Preprocessed/test_6_no_stop.txt", encoding='utf-8', errors='ignore')

tokenizer = SinhalaTweetTokenizer()

print("Loaded")

sentences = []
for line in f_1:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 1")

for line in f_2:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 2")

for line in f_3:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 3")

for line in f_4:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 4")

for line in f_5:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 5")

for line in f_6:
    line = line.rstrip()
    sentences.append(tokenizer.tokenize(line))

print("Finished File 6")

pickle_out = open("sentences.pickle","wb")
pickle.dump(sentences, pickle_out)
pickle_out.close()

#count tokens, each one being a sentence
token_count = sum([len(sentence) for sentence in sentences])
print("The Sinhala corpus contains {0:,} tokens".format(token_count))


model = fasttext.FastText(size=300, window=10, min_count=1, workers=8, sg=1)

model.build_vocab(sentences = sentences)

model.train(sentences=sentences, total_examples=len(sentences), epochs=50)

#save model
if not os.path.exists("trained_fasttext_300_nsw"):
    os.makedirs("trained_fasttext_300_nsw")


model.save(os.path.join("trained_fasttext_300_nsw", "fasttext_100_nsw.w2v"))



# model = fasttext.FastText(size=200, window=5, min_count=3)
# model.build_vocab(sentences = sentences)
# model.train(sentences=sentences, total_examples=len(sentences), epochs=10)
#
# #save model
# if not os.path.exists("trained_fasttext_200"):
#     os.makedirs("trained_fasttext_200")
#
#
# model.save(os.path.join("trained_fasttext_200", "fasttext_200.w2v"))
#
#
# model = fasttext.FastText(size=300, window=5, min_count=3)
# model.build_vocab(sentences = sentences)
# model.train(sentences=sentences, total_examples=len(sentences), epochs=10)
#
# #save model
# if not os.path.exists("trained_fasttext_300"):
#     os.makedirs("trained_fasttext_300")
#
#
# model.save(os.path.join("trained_fasttext_300", "fasttext_300.w2v"))

