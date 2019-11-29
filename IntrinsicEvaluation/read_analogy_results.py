__author__ = 'kjtdi'
import codecs

file_to_read = codecs.open("./Analogy Results/test_fasttext_300_pretrained.txt", encoding='utf-8', errors='ignore')

total_correct_i = 0
total_qs_i = 0

total_correct_d = 0
total_qs_d = 0

total_correct_e = 0
total_qs_e = 0

i_start = False
d_start = False
e_start = False

correct = 0
qs = 0

first_line = False

for line in file_to_read:
    line = line.rstrip()

    if(line.startswith("I")):
        print(line)
        first_line = False
        i_start = True
        correct = 0
        qs = 0

    if(line.startswith("D")):
        print(line)
        first_line = False
        d_start = True
        correct = 0
        qs = 0

    if(line.startswith("E")):
        print(line)
        first_line = False
        e_start = True
        correct = 0
        qs = 0

    if(i_start and line.isdigit() and not(first_line)):
        first_line = True
        correct = int(line)
        total_correct_i += correct
        continue

    if(i_start and line.isdigit() and first_line):
        qs = int(line)
        total_qs_i += qs
        print(round((correct/qs)*100,2))
        continue

    if(d_start and line.isdigit() and not(first_line)):
        first_line = True
        correct = int(line)
        total_correct_d += correct
        #print("D Correct", correct)
        continue

    if(d_start and line.isdigit() and first_line):
        qs = int(line)
        total_qs_d += qs
        print(round((correct/qs)*100,2))
        continue

    if(e_start and line.isdigit() and not(first_line)):
        first_line = True
        correct = int(line)
        total_correct_e += correct
        #print("E Correct", correct)
        continue

    if(e_start and line.isdigit() and first_line):
        qs = int(line)
        total_qs_e += qs
        print(round((correct/qs)*100,2))
        continue

    if(line == ""):
        i_start = False
        d_start = False
        e_start = False


print("Avg Inflectional", round((total_correct_i/total_qs_i)*100,2))
print("Avg Dericational", round((total_correct_d/total_qs_d)*100,2))
print("Avg Encyclopedi", round((total_correct_e/total_qs_e)*100,2))

