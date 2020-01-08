#You can use this script to evaluate glove model in terms of analogy instrinsic evaluation

import codecs
from os import listdir
from os.path import isfile, join
from glove import Corpus, Glove
from scipy.spatial import distance
import multiprocessing as mp
import analogy_tasks

#this array of paths consists of analogy questions
folder_paths = ["./Inflectional"]

#this file is used to record results of the evaluation
f_w = codecs.open("test.txt", 'w', encoding='utf-8')

#load glove model
model = Glove.load("../NoiseRemoval/trained_glove_300/glove_300.model")

print("Model Loaded")

pool = mp.Pool(mp.cpu_count())

for folder_path in folder_paths:
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    f_w.write(folder_path + "\n")

    for file_name in files:

        f_w.write(file_name + "\n")

        word_pairs = []
        file_to_read = codecs.open(join(folder_path, file_name), encoding='utf-8', errors='ignore')

        i = 0
        all_word_pairs = []
        #read analogy question file line by line and extract words in the analogy question
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

        #process analogy questions simultaneously with availbale cpu cores
        results = pool.map(analogy_tasks.count_analogy_results, [analogy_question for analogy_question in all_word_pairs])

        #record total score
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