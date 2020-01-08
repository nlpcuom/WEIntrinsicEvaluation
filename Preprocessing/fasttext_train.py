from __future__ import absolute_import, division, print_function

#This script is for training fasttext embeddings.
#First we read preprocessed text files consists of sentences in each line and push tokenized sentences to an array.
#Then train fasttext models with preferred hyper parameters and save trained model into the disk

from sinling.sinhala.tokenizer import SinhalaTweetTokenizer

#encoding. word encodig
import codecs
import os
import pickle
import gensim.models.fasttext as fasttext

#read corpus files one by one
f_1 = codecs.open("Preprocessed/test_1_no_stop.txt", encoding='utf-8', errors='ignore')
f_2 = codecs.open("Preprocessed/test_2_no_stop.txt", encoding='utf-8', errors='ignore')
f_3 = codecs.open("Preprocessed/test_3_no_stop.txt", encoding='utf-8', errors='ignore')
f_4 = codecs.open("Preprocessed/test_4_no_stop.txt", encoding='utf-8', errors='ignore')
f_5 = codecs.open("Preprocessed/test_5_no_stop.txt", encoding='utf-8', errors='ignore')
f_6 = codecs.open("Preprocessed/test_6_no_stop.txt", encoding='utf-8', errors='ignore')

tokenizer = SinhalaTweetTokenizer()

print("Loaded")

#tokenize sentences and push into an array
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

#count tokens, each one being a sentence
token_count = sum([len(sentence) for sentence in sentences])
print("The Sinhala corpus contains {0:,} tokens".format(token_count))


#define fasttext model. User sg (0 or 1) argument to choose between CBOW and Skipgram
model = fasttext.FastText(size=300, window=10, min_count=1, workers=8, sg=1)

model.build_vocab(sentences = sentences)

#train fasttext model
model.train(sentences=sentences, total_examples=len(sentences), epochs=50)

#save model
if not os.path.exists("trained_fasttext_300_nsw"):
    os.makedirs("trained_fasttext_300_nsw")


model.save(os.path.join("trained_fasttext_300_nsw", "fasttext_100_nsw.w2v"))

