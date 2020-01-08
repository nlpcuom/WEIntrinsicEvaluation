
import pandas as pd
import codecs
import string

comments = pd.read_csv("comments_no_punctuations.csv", ";")
f_w = codecs.open("comments_no_punctuations_test.csv", 'w', 'utf-8')
f_w.write("docid;comment;label"+"\n")

i = 0
for index, row in comments.iterrows():
    comment = row['comment']
    comment_without_punctuation = str(comment).translate(str.maketrans('', '', string.punctuation))

    f_w.write(str(row['docid'])+";"+str(comment_without_punctuation)+";"+str(row['label'])+"\n")

f_w.close()