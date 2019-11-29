__author__ = 'kjtdi'
import codecs
import re

f_1 = codecs.open("data/news_1.txt", encoding='utf-8', errors='ignore')
f_2 = codecs.open("data/official_docs_1.txt", encoding='utf-8', errors='ignore')
f_3 = codecs.open("data/wiki_1.txt", encoding='utf-8', errors='ignore')
f_train = codecs.open("train_data.txt", 'w', encoding='utf-8')
f_test = codecs.open("test_data.txt", 'w', encoding='utf-8')
f_e = codecs.open("error.txt", 'w', encoding='utf-8')

sentences = []
sentences_test = []
i = 0
for line in f_1:
    elments = re.split('\s+', line.rstrip())
    if(len(elments) == 2):
        word = elments[0]
        tag = elments[1]
        if(i>10000):
            sentences.append([word, tag])
        else:
            sentences_test.append([word, tag])
    else:
        f_e.write(line)
        print(i)
        print("tiggered")
    i += 1

print("Finished File 1")

i = 0
for line in f_2:
    elments = re.split('\s+', line.rstrip())
    if(len(elments) == 2):
        word = elments[0]
        tag = elments[1]
        if(i>10000):
            sentences.append([word, tag])
        else:
            sentences_test.append([word, tag])
    else:
        print(i)
        print("tiggered")
    i += 1

print("Finished File 2")

i = 0
for line in f_3:
    elments = re.split('\s+', line.rstrip())
    if(len(elments) == 2):
        word = elments[0]
        tag = elments[1]
        if(i>10000):
            sentences.append([word, tag])
        else:
            sentences_test.append([word, tag])
    else:
        print(i)
        print("tiggered")
    i += 1

for sentence in sentences:
    f_train.write(sentence[0]+"\t"+sentence[1]+"\n")

for sentence in sentences_test:
    f_test.write(sentence[0]+"\t"+sentence[1]+"\n")

f_train.close()
f_test.close()
f_e.close()