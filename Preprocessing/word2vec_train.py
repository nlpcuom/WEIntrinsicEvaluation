from __future__ import absolute_import, division, print_function

from sinling.sinhala.tokenizer import SinhalaTweetTokenizer

#encoding. word encodig
import codecs
#finds all pathnames matching a pattern, like regex
import glob
#log events for libraries
import logging
#concurrency
import multiprocessing
#dealing with operating system , like reading file
import os
#pretty print, human readable
import pprint
#regular expressions
import re

#natural language toolkit
import nltk
#word 2 vec
import gensim.models.word2vec as w2v
#dimensionality reduction
import sklearn.manifold
#math
import numpy as np
#plotting
import matplotlib.pyplot as plt
#parse dataset
import pandas as pd
#visualization
import seaborn as sns
import pickle

f_1 = codecs.open("Preprocessed/test_1_no_stop.txt", encoding='utf-8', errors='ignore')
f_2 = codecs.open("Preprocessed/test_2_no_stop.txt", encoding='utf-8', errors='ignore')
f_3 = codecs.open("Preprocessed/test_3_no_stop.txt", encoding='utf-8', errors='ignore')
f_4 = codecs.open("Preprocessed/test_4_no_stop.txt", encoding='utf-8', errors='ignore')
f_5 = codecs.open("Preprocessed/test_5_no_stop.txt", encoding='utf-8', errors='ignore')
f_6 = codecs.open("Preprocessed/test_6_no_stop.txt", encoding='utf-8', errors='ignore')

tokenizer = SinhalaTweetTokenizer()

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

# pickle_in = open("sentences.pickle","rb")
# sentences = pickle.load(pickle_in)

#count tokens, each one being a sentence
token_count = sum([len(sentence) for sentence in sentences])
print("The Sinhala corpus contains {0:,} tokens".format(token_count))

#step 2 build our model, another one is Glove
#define hyperparameters

# Dimensionality of the resulting word vectors.
#more dimensions mean more traiig them, but more generalized
num_features = 300

#
# Minimum word count threshold.
min_word_count = 1

# Number of threads to run in parallel.
num_workers = multiprocessing.cpu_count()

# Context window length.
context_size = 10

# Downsample setting for frequent words.
#rate 0 and 1e-5
#how often to use
downsampling = 1e-3

# Seed for the RNG, to make the results reproducible.
seed = 1


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


# #load model
# thrones2vec = w2v.Word2Vec.load(os.path.join("trained", "thrones2vec.w2v"))
#
#
# #squash dimensionality to 2
# #https://www.oreilly.com/learning/an-illustrated-introduction-to-the-t-sne-algorithm
# tsne = sklearn.manifold.TSNE(n_components=2, random_state=0)
#
#
# #put it all into a giant matrix
# all_word_vectors_matrix = thrones2vec.syn0
#
#
# #train t sne
# all_word_vectors_matrix_2d = tsne.fit_transform(all_word_vectors_matrix)
#
#
# #plot point in 2d space
# points = pd.DataFrame(
#     [
#         (word, coords[0], coords[1])
#         for word, coords in [
#             (word, all_word_vectors_matrix_2d[thrones2vec.vocab[word].index])
#             for word in thrones2vec.vocab
#         ]
#     ],
#     columns=["word", "x", "y"]
# )
#
#
# points.head(10)
#
#
# #plot
# sns.set_context("poster")
#
#
# points.plot.scatter("x", "y", s=10, figsize=(20, 12))
#
#
# def plot_region(x_bounds, y_bounds):
#     slice = points[
#         (x_bounds[0] <= points.x) &
#         (points.x <= x_bounds[1]) &
#         (y_bounds[0] <= points.y) &
#         (points.y <= y_bounds[1])
#     ]
#
#     ax = slice.plot.scatter("x", "y", s=35, figsize=(10, 8))
#     for i, point in slice.iterrows():
#         ax.text(point.x + 0.005, point.y + 0.005, point.word, fontsize=11)
#
#
# plot_region(x_bounds=(4.0, 4.2), y_bounds=(-0.5, -0.1))
#
#
# plot_region(x_bounds=(0, 1), y_bounds=(4, 4.5))
#
#
# thrones2vec.most_similar("Stark")
#
#
# thrones2vec.most_similar("Aerys")
#
#
# thrones2vec.most_similar("direwolf")
#
#
# #distance, similarity, and ranking
# def nearest_similarity_cosmul(start1, end1, end2):
#     similarities = thrones2vec.most_similar_cosmul(
#         positive=[end2, start1],
#         negative=[end1]
#     )
#     start2 = similarities[0][0]
#     print("{start1} is related to {end1}, as {start2} is related to {end2}".format(**locals()))
#     return start2
#
#
# nearest_similarity_cosmul("Stark", "Winterfell", "Riverrun")
# nearest_similarity_cosmul("Jaime", "sword", "wine")
# nearest_similarity_cosmul("Arya", "Nymeria", "dragons")

