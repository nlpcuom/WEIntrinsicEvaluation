__author__ = 'kjtdi'

#We use this script to evaluate glove model in terms of relatedness task
from gensim import utils, matutils
from scipy import stats
from numpy import dot

from glove import Glove
import codecs

#Results record in this file
f_w = codecs.open("./results_relatedness_glove_300.txt", 'w', encoding='utf-8')

#load model
model = Glove.load("../NoiseRemoval/trained_glove_300/glove_300.model")

#measure similarity between two unit vectors
def similarity(w1, w2):
    return dot(matutils.unitvec(w1), matutils.unitvec(w2))

#print results
def log_evaluate_word_pairs(pearson, spearman, oov, pairs):
    f_w.write('Pearson correlation coefficient against %s: %.4f '+pairs +" "+str(pearson[0]) +"\n")
    f_w.write('Spearman rank-order correlation coefficient against %s: %.4f '+ pairs +" "+ str(spearman[0])+"\n")
    f_w.write('Pairs with unknown words ratio: %.1f%% '+  str(oov)+"\n")


def evaluate_word_pairs(pairs, delimiter='\t'):
    similarity_gold = []
    similarity_model = []
    oov = 0

    with codecs.open(pairs, encoding='utf-8', errors='ignore') as f:
        for line in f:
            print("Process")
            line = line.rstrip()
            a, b, sim = line.split(delimiter)
            sim = float(sim)
            a = a.strip()
            b = b.strip()
            if a not in model.dictionary or b not in model.dictionary:
                oov += 1
                print('skipping line #%d with OOV words: %s', line)
            else:
                similarity_gold.append(sim)  # Similarity from the dataset
                print(sim)
                print(similarity(model.word_vectors[model.dictionary[a]], model.word_vectors[model.dictionary[b]]))
                similarity_model.append(similarity(model.word_vectors[model.dictionary[a]], model.word_vectors[
                    model.dictionary[b]]))  # Similarity from the model

    # Meaure pearson and spearman correlations among among similarity measurements given by the golden standard and the model
    spearman = stats.spearmanr(similarity_gold, similarity_model)
    pearson = stats.pearsonr(similarity_gold, similarity_model)
    oov_ratio = float(oov) / (len(similarity_gold) + oov) * 100

    f_w.write('Pearson correlation coefficient against %s: %f with p-value %f ' + pairs + " " + str(pearson[0]) + " " + str(pearson[1])+"\n")
    f_w.write('Spearman rank-order correlation coefficient against %s: %f with p-value %f '+ " " +pairs+ " " + str(spearman[0])+ " " + str(spearman[1])
    +"\n")
    f_w.write('Pairs with unknown words: %d ' + str(oov)+"\n")

    log_evaluate_word_pairs(pearson, spearman, oov_ratio, pairs)
    return pearson, spearman, oov_ratio

evaluate_word_pairs("./WordSim/wordsim353_sinhala.txt", "\t")