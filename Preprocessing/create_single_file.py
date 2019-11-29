__author__ = 'kjtdi'
import codecs

f_1 = codecs.open("Preprocessed/test_1.txt", encoding='utf-8', errors='ignore')
f_2 = codecs.open("Preprocessed/test_2.txt", encoding='utf-8', errors='ignore')
f_3 = codecs.open("Preprocessed/test_3.txt", encoding='utf-8', errors='ignore')
f_4 = codecs.open("Preprocessed/test_4.txt", encoding='utf-8', errors='ignore')
f_5 = codecs.open("Preprocessed/test_5.txt", encoding='utf-8', errors='ignore')
f_6 = codecs.open("Preprocessed/test_6.txt", encoding='utf-8', errors='ignore')

f_w = codecs.open("test.txt", 'w', encoding='utf-8')

for line in f_1:
    f_w.write(line)

for line in f_2:
    f_w.write(line)

for line in f_3:
    f_w.write(line)

for line in f_4:
    f_w.write(line)

for line in f_5:
    f_w.write(line)

for line in f_6:
    f_w.write(line)


f_w.close()
f_1.close()
f_2.close()
f_3.close()
f_4.close()
f_5.close()
f_6.close()