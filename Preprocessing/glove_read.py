__author__ = 'kjtdi'
import codecs
from glove import Corpus, Glove
from scipy.spatial import distance

glove = Glove.load("glove.model")
print(len(glove.word_vectors[glove.dictionary['වැනි']]))

def find_closest_embeddings(embedding):
    return sorted(glove.dictionary.keys(),
                  key=lambda word: distance.euclidean(glove.word_vectors[glove.dictionary[word]], embedding))


def analogy_task(a,b,c,d):
    print(find_closest_embeddings(
    glove.word_vectors[glove.dictionary[c]] - glove.word_vectors[glove.dictionary[a]] + glove.word_vectors[glove.dictionary[b]]))



