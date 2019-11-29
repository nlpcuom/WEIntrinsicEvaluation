import codecs
from os import listdir
from os.path import isfile, join
# from gensim.models import word2vec
import gensim.models.fasttext as fasttext
from glove import Corpus, Glove
from scipy.spatial import distance
import multiprocessing as mp
import analogy_tasks

folder_paths = ["./Inflectional"]
f_w = codecs.open("test.txt", 'w', encoding='utf-8')

model = Glove.load("../NoiseRemoval/trained_glove_300/glove_300.model")

print("Model Loaded")

pool = mp.Pool(mp.cpu_count())

def find_closest_embeddings(embedding):
    return sorted(model.dictionary.keys(),
                  key=lambda word: distance.euclidean(model.word_vectors[model.dictionary[word]], embedding))


def analogy_task(a,b,c):
    print(a,b,c)
    if (a in model.dictionary) and (b in model.dictionary) and (c in model.dictionary):
        return find_closest_embeddings(
        model.word_vectors[model.dictionary[c]] - model.word_vectors[model.dictionary[a]] + model.word_vectors[model.dictionary[b]])[:5]
    else:
        return []

def count_analogy_results(analogy_question):
    results = analogy_task(analogy_question[0],analogy_question[1], analogy_question[2])
    print("Results ", results)
    print("Question ", analogy_question)
    found_true = False
    for result in results:
        if (result[0] == analogy_question[3]):
            found_true = True

    return found_true


for folder_path in folder_paths:
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    f_w.write(folder_path + "\n")

    for file_name in files:

        f_w.write(file_name + "\n")

        word_pairs = []
        file_to_read = codecs.open(join(folder_path, file_name), encoding='utf-8', errors='ignore')

        i = 0
        all_word_pairs = []
        for line in file_to_read:
            line = line.rstrip()
            word_pairs = line.split("\t")
            left_words = word_pairs[0].split(",")
            right_words = word_pairs[1].split(",")

            all_word_pairs.append([left_words[0],left_words[1], right_words[0], right_words[1]])

            i += 1
            print(i)

            if i == 10:
                break


        results = pool.map(analogy_tasks.count_analogy_results, [analogy_question for analogy_question in all_word_pairs])
        # for analogy_question in all_word_pairs:
        #     count_analogy_results(analogy_question)

        score = 0
        for result in results:
            if result:
                score += 1

        f_w.write(str(score) + "\n")
        f_w.write(str(i) + "\n")
        f_w.write("\n")

    f_w.write("\n")
    f_w.write("\n")

f_w.close()