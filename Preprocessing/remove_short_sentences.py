__author__ = 'kjtdi'
#some of the sentences are too short and wrongly seperated into new lines.
#need to remove those short sentences before feeding to embedding models

import codecs

f = codecs.open("Preprocessed/wikipedia_si_filtered_1.txt", encoding='utf-8', errors='ignore')
f_w = codecs.open("test_7.txt", 'w+', encoding='utf-8')

i=0
for line in f:
    print(len(line))
    if(len(line) > 30):
        f_w.write(line)


f_w.close()
f.close()