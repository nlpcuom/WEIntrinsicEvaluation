__author__ = 'kjtdi'
import codecs
from os import listdir
from os.path import isfile, join
from itertools import permutations

# f_1 = codecs.open("Preprocessed/test_1.txt", encoding='utf-8', errors='ignore')
file_name = "E12 [ institute - head ] completed.txt"
f_w = codecs.open(file_name, 'w', encoding='utf-8')
f_t = codecs.open("test.txt", 'w', encoding='utf-8')

folder_path_1 = "D:/NLP/Datasets/BATS_3.0/v2/Encyclopedic"

files = [f for f in listdir(folder_path_1) if isfile(join(folder_path_1, f))]

word_pairs = []
file_to_read = codecs.open(join(folder_path_1, file_name), encoding='utf-8', errors='ignore')
for line in file_to_read:
    line = line.rstrip()
    word_pair = line.split(" - ")
    word_pairs.append(word_pair)


def writeParirs():
    for word_pair in word_pairs:
        if(len(word_pair)==2):
            f_t.write(word_pair[0] + " " + word_pair[1] + "\n")

        else:
            f_t.write("triggered")
            f_t.write(word_pair[0] + "\n")

    f_t.close()

def writePermutations():

    word_permutations = permutations(word_pairs, 2)

    for permutation in word_permutations:
        first_pair = permutation[0]
        second_pair = permutation[1]
        print(len(first_pair),len(second_pair))

        f_w.write(first_pair[0]+","+first_pair[1]+"\t"+second_pair[0]+","+second_pair[1]+"\n")

    f_w.close()

writeParirs()
writePermutations()
