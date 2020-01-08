__author__ = 'kjtdi'
from sinling.sinhala.tokenizer import SinhalaTweetTokenizer

import codecs

#some senetences include only numbers or mostly numbers. We remove those sentences
f = codecs.open("wikipedia_si_filtered_tokenized.txt", encoding='utf-8', errors='ignore')
f_w = codecs.open("Preprocessed/wikipedia_si_filtered_1.txt", 'w', encoding='utf-8')

i=0
for line in f:
    num_occurances = line.count('#')
    total_chars = len(line)
    propotion_numbers = num_occurances/total_chars
    if(propotion_numbers < 0.3):
        f_w.write(line)


f_w.close()
f.close()
