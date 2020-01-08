from __future__ import absolute_import, division, print_function

#This script is for training word2vec CBOW and skipgram embeddings.
#First we read preprocessed text files consists of sentences in each line and push tokenized sentences to an array.
#Then train word2vec models with preferred hyper parameters and save trained model into the disk

from sinling.sinhala.tokenizer import SinhalaTweetTokenizer

#encoding. word encodig
import codecs
#concurrency
import multiprocessing
#dealing with operating system , like reading file
import os
#word 2 vec
import gensim.models.word2vec as w2v
import pickle

f_1 = codecs.open("Preprocessed/test_1_no_stop.txt", encoding='utf-8', errors='ignore')
f_2 = codecs.open("Preprocessed/test_2_no_stop.txt", encoding='utf-8', errors='ignore')
f_3 = codecs.open("Preprocessed/test_3_no_stop.txt", encoding='utf-8', errors='ignore')
f_4 = codecs.open("Preprocessed/test_4_no_stop.txt", encoding='utf-8', errors='ignore')
f_5 = codecs.open("Preprocessed/test_5_no_stop.txt", encoding='utf-8', errors='ignore')
f_6 = codecs.open("Preprocessed/test_6_no_stop.txt", encoding='utf-8', errors='ignore')

tokenizer = SinhalaTweetTokenizer()

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

#if you want you can save the processed corpus into seperate file in the disk so that you can save your time next time training
pickle_out = open("sentences.pickle","wb")
pickle.dump(sentences, pickle_out)
pickle_out.close()


#count tokens, each one being a sentence
token_count = sum([len(sentence) for sentence in sentences])
print("The Sinhala corpus contains {0:,} tokens".format(token_count))

#define hyperparameters

# Dimensionality of the resulting word vectors.
num_features = 300

# Minimum word count threshold.
min_word_count = 1

# Number of threads to run in parallel.
num_workers = multiprocessing.cpu_count()

# Context window length.
context_size = 10

# Downsample setting for frequent words.
downsampling = 1e-3

# Seed for the RNG, to make the results reproducible.
seed = 1

#define word2vec with preferred hyper parameters. Use sg (0 or 1) argument to choose between CBOW and Skipgram
sinhalaword2vec = w2v.Word2Vec(
    sg=1,
    seed=seed,
    workers=num_workers,
    size=num_features,
    min_count=min_word_count,
    window=context_size,
    sample=downsampling,
    iter = 20
)

sinhalaword2vec.build_vocab(sentences)

print("Word2Vec vocabulary length:", len(sinhalaword2vec.wv.vocab))
print("Model Corpus Count", sinhalaword2vec.corpus_count)
print("Iterations", sinhalaword2vec.iter)

#train model on sentneces
sinhalaword2vec.train(sentences, total_examples=sinhalaword2vec.corpus_count, epochs=sinhalaword2vec.iter)


#save model
if not os.path.exists("trained_word2vec_300_nsw"):
    os.makedirs("trained_word2vec_300_nsw")


sinhalaword2vec.save(os.path.join("trained_word2vec_300_nsw", "word2vec_300_nsw.w2v"))

