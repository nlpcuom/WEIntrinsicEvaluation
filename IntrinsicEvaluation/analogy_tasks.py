__author__ = 'kjtdi'
from glove import Corpus, Glove
from scipy.spatial import distance

model = Glove.load("../NoiseRemoval/trained_glove_300/glove_300.model")

def find_closest_embeddings(embedding):
    return sorted(model.dictionary.keys(),
                  key=lambda word: distance.euclidean(model.word_vectors[model.dictionary[word]], embedding))


def analogy_task(a,b,c):
    print("Question ", a,b,c)
    if (a in model.dictionary) and (b in model.dictionary) and (c in model.dictionary):
        return find_closest_embeddings(
        model.word_vectors[model.dictionary[c]] - model.word_vectors[model.dictionary[a]] + model.word_vectors[model.dictionary[b]])[:5]
    else:
        return []

def count_analogy_results(analogy_question):
    results = analogy_task(analogy_question[0],analogy_question[1], analogy_question[2])
    print("Restul ", results)
    found_true = False
    for result in results:
        if (result == analogy_question[3]):
            print("Found")
            found_true = True

    return found_true