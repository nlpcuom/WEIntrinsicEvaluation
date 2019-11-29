import codecs
from os import listdir
from os.path import isfile, join
import gensim.models.fasttext as fasttext
from gensim.models import word2vec

folder_paths = ["./Inflectional", "./Derivational" ,"./Encyclopedic"]
model = word2vec.Word2Vec.load("../NoiseRemoval/trained_word2vec_300/word2vec_300.w2v")
model = fasttext.FastText.load("../NoiseRemoval/trained_fasttext_300/fasttext_300.w2v")
f_w = codecs.open("test.txt", 'w', encoding='utf-8')

for folder_path in folder_paths:
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    f_w.write(folder_path + "\n")

    for file_name in files:

        f_w.write(file_name + "\n")

        word_pairs = []
        file_to_read = codecs.open(join(folder_path, file_name), encoding='utf-8', errors='ignore')

        i = 0
        score = 0
        for line in file_to_read:
            line = line.rstrip()
            word_pairs = line.split("\t")
            left_words = word_pairs[0].split(",")
            right_words = word_pairs[1].split(",")

            if((right_words[0] in model.wv.vocab) and (left_words[0] in model.wv.vocab) and (left_words[1] in model.wv.vocab)):
                results = model.most_similar_cosmul(positive=[right_words[0], left_words[1]], negative=[left_words[0]], topn = 5)
                for result in results:
                    if (result[0] == right_words[1]):
                        score += 1

            i += 1
            print(i)

        f_w.write(str(score) + "\n")
        f_w.write(str(i) + "\n")
        f_w.write("\n")

    f_w.write("\n")
    f_w.write("\n")

f_w.close()