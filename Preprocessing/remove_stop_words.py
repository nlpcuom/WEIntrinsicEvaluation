__author__ = 'kjtdi'
#encoding. word encodig
import codecs

f_n = codecs.open("Preprocessed/test_6_no_stop.txt", 'w', encoding='utf-8')
f_stop_words = codecs.open("stop words.txt", encoding='utf-8', errors='ignore')

print("Loaded")

stop_words = []
for line in f_stop_words:
    stop_word = line.rstrip()
    stop_words.append(stop_word)

print("Finished File 1")

with codecs.open("Preprocessed/test_6.txt", encoding='utf-8', errors='ignore') as f:
    text = f.read()
    i = 0
    for stop_word in stop_words:
        text = text.replace(' ' + stop_word + ' ', ' ')
        i += 1
        print(i)

    f_n.write(text)

f_n.close()

# for line in f_2:
#     line = line.rstrip()
#     sentences.append(tokenizer.tokenize(line))
#
# print("Finished File 2")
#
# for line in f_3:
#     line = line.rstrip()
#     sentences.append(tokenizer.tokenize(line))
#
# print("Finished File 3")
#
# for line in f_4:
#     line = line.rstrip()
#     sentences.append(tokenizer.tokenize(line))
#
# print("Finished File 4")
#
# for line in f_5:
#     line = line.rstrip()
#     sentences.append(tokenizer.tokenize(line))
#
# print("Finished File 5")
#
# for line in f_6:
#     line = line.rstrip()
#     sentences.append(tokenizer.tokenize(line))
#
# print("Finished File 6")