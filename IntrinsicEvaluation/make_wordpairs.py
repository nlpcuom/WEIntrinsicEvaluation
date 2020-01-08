__author__ = 'kjtdi'
#We use this to make analogy questions using the word pairs in each relationship file.
#After reading all word pairs in a relationship we make use of python's permutation function to make analogy questions.

import codecs
from os.path import isfile, join
from itertools import permutations

# source file consits of word pairs
file_name = "E12 [ institute - head ] completed.txt"
f_w = codecs.open("Analogy Questions.txt", 'w', encoding='utf-8')

folder_path_1 = "D:/NLP/Datasets/BATS_3.0/v2/Encyclopedic"

#read word pairs
word_pairs = []
file_to_read = codecs.open(join(folder_path_1, file_name), encoding='utf-8', errors='ignore')
for line in file_to_read:
    line = line.rstrip()
    word_pair = line.split(" - ")
    word_pairs.append(word_pair)

#build analogy questions
def writePermutations():

    word_permutations = permutations(word_pairs, 2)

    for permutation in word_permutations:
        first_pair = permutation[0]
        second_pair = permutation[1]
        print(len(first_pair),len(second_pair))

        f_w.write(first_pair[0]+","+first_pair[1]+"\t"+second_pair[0]+","+second_pair[1]+"\n")

    f_w.close()

writePermutations()
