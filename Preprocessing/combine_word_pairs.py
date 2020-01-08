from sinling.sinhala.tokenizer import SinhalaTweetTokenizer
import codecs

f_1 = codecs.open("Preprocessed/test_1.txt", encoding='utf-8', errors='ignore')
f_2 = codecs.open("Preprocessed/test_2.txt", encoding='utf-8', errors='ignore')
f_3 = codecs.open("Preprocessed/test_3.txt", encoding='utf-8', errors='ignore')
f_4 = codecs.open("Preprocessed/test_4.txt", encoding='utf-8', errors='ignore')
f_5 = codecs.open("Preprocessed/test_5.txt", encoding='utf-8', errors='ignore')
f_6 = codecs.open("Preprocessed/test_7.txt", encoding='utf-8', errors='ignore')

tokenizer = SinhalaTweetTokenizer()

sentences = []

for line in f_6:
    line = line.rstrip()
    sentences.append(line.split(" "))

print("Finished File 6")

f_w = codecs.open("test_combined_pairs.txt", 'w', encoding='utf-8')

prefix_list = ['වඩා']

suffix_list = ['කරනවා']

new_sentences = []
j = 0
for sentence in sentences:
    temp_sentence = []
    [temp_sentence.append(word) for word in sentence]
    k = 0
    print(len(sentence))
    for i in range(len(sentence)):
        if i > 0:
            prefix = sentence[i-1]
            if prefix in prefix_list:
                new_word = sentence[i-1] + "_" + sentence[i]
                temp_sentence[k-1] = new_word
                del temp_sentence[k]
                k -= 1
        if i < (len(sentence)-1):
            suffix = sentence[i+1]
            if suffix in suffix_list:
                new_word = sentence[i] + "_" + sentence[i+1]
                temp_sentence[k] = new_word
                del temp_sentence[k+1]
                k -= 1

        k += 1

    new_sentences.append(temp_sentence)


for sentence in new_sentences:
    print(len(sentence))
    line = ""
    i = 0
    for i in range(len(sentence)-1):
        line += sentence[i]+" "

    line += sentence[len(sentence)-1] + "\n"
    f_w.write(line)

f_w.close()

