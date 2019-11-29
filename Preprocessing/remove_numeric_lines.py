__author__ = 'kjtdi'
from sinling.sinhala.tokenizer import SinhalaTweetTokenizer

import codecs

f = codecs.open("wikipedia_si_filtered_tokenized.txt", encoding='utf-8', errors='ignore')
f_w = codecs.open("Preprocessed/wikipedia_si_filtered_1.txt", 'w', encoding='utf-8')

i=0
for line in f:
    num_occurances = line.count('#')
    total_chars = len(line)
    propotion_numbers = num_occurances/total_chars
    if(propotion_numbers < 0.3):
        f_w.write(line)

# tokenizer = SinhalaTweetTokenizer()
#
# i=0
# sentences = []
# for line in f:
#     line = line.rstrip()
#     sentences.append(tokenizer.tokenize(line))
#
#     i += 1
#     if(i>30):
#         break


f_w.close()
f.close()
